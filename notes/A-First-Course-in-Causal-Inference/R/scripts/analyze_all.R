library(Matching)
library(ggplot2)
library(dplyr)
library(sandwich)
library(lmtest)

data(lalonde)

# 提取变量
z <- lalonde$treat
y <- lalonde$re78
n1 <- sum(z)
n0 <- length(z) - n1
n <- length(z)

cat("===========================================\n")
cat("     LaLonde 数据分析 - 因果推断教材\n")
cat("===========================================\n\n")

cat("=== 1. 数据基本信息 ===\n")
cat("样本量:", n, "\n")
cat("处理组 (n1):", n1, "\n")
cat("对照组 (n0):", n0, "\n\n")

# 描述性统计
treatment <- lalonde[lalonde$treat == 1, ]
control <- lalonde[lalonde$treat == 0, ]

cat("=== 2. 处理组结果变量 (re78) ===\n")
cat("均值:", mean(treatment$re78), "\n")
cat("标准差:", sd(treatment$re78), "\n")
cat("中位数:", median(treatment$re78), "\n")
cat("最小值:", min(treatment$re78), "\n")
cat("最大值:", max(treatment$re78), "\n\n")

cat("=== 3. 对照组结果变量 (re78) ===\n")
cat("均值:", mean(control$re78), "\n")
cat("标准差:", sd(control$re78), "\n")
cat("中位数:", median(control$re78), "\n")
cat("最小值:", min(control$re78), "\n")
cat("最大值:", max(control$re78), "\n\n")

# FRT 检验统计量
cat("=== 4. FRT 检验统计量 ===\n")
tauhat <- mean(y[z == 1]) - mean(y[z == 0])
s1_sq <- var(y[z == 1])
s0_sq <- var(y[z == 0])
t_stat <- tauhat / sqrt(s1_sq / n1 + s0_sq / n0)
cat("差值均值 tauhat:", tauhat, "\n")
cat("学生化统计量 t:", t_stat, "\n")

# Wilcoxon 秩和
ranks <- rank(y)
W <- sum(ranks[z == 1])
cat("Wilcoxon 秩和 W:", W, "\n")

# KS 统计量
treatment_y <- y[z == 1]
control_y <- y[z == 0]
ks_result <- ks.test(treatment_y, control_y)
D <- ks_result$statistic
cat("KS 统计量 D:", D, "\n\n")

# 置换检验
cat("=== 5. FRT 置换检验 ===\n")
set.seed(42)
B <- 10000
perm_tauhat <- numeric(B)
for (b in 1:B) {
  z_perm <- sample(z)
  perm_tauhat[b] <- mean(y[z_perm == 1]) - mean(y[z_perm == 0])
}
p_value <- mean(abs(perm_tauhat) >= abs(tauhat))
cat("置换检验 p 值 (双侧):", p_value, "\n\n")

# Neymanian 推断
cat("=== 6. Neymanian 推断 ===\n")
vhat <- s1_sq / n1 + s0_sq / n0
se <- sqrt(vhat)
cat("点估计 tauhat:", tauhat, "\n")
cat("标准误:", se, "\n")
cat("95% CI: [", tauhat - 1.96*se, ",", tauhat + 1.96*se, "]\n")
cat("p 值:", 2 * (1 - pnorm(abs(tauhat / se))), "\n\n")

# OLS 比较
cat("=== 7. OLS 比较 ===\n")
model <- lm(re78 ~ treat, data = lalonde)
coef_default <- summary(model)$coefficients["treat", ]
coef_robust <- coeftest(model, vcov = vcovHC(model, type = "HC2"))["treat", ]
cat("OLS 默认 - 点估计:", coef_default["Estimate"], ", SE:", coef_default["Std. Error"], "\n")
cat("OLS HC2 稳健 - 点估计:", coef_robust["Estimate"], ", SE:", coef_robust["Std. Error"], "\n\n")

# ============ 可视化部分 ============
cat("=== 8. 生成可视化图表 ===\n")

dir.create("R/figures", showWarnings = FALSE)

# 图1: 箱线图
png("R/figures/01_boxplot_comparison.png", width = 800, height = 600, res = 100)
ggplot(lalonde, aes(x = factor(treat), y = re78, fill = factor(treat))) +
  geom_boxplot() +
  scale_fill_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                   labels = c("对照组", "处理组")) +
  labs(title = "LaLonde 数据：处理组与对照组收入比较",
       x = "组别 (0=对照组, 1=处理组)",
       y = "1978 年真实收入 ($)",
       fill = "组别") +
  theme_minimal(base_size = 14) +
  theme(legend.position = "bottom")
dev.off()
cat("已生成: 01_boxplot_comparison.png\n")

# 图2: 直方图
png("R/figures/02_histogram_comparison.png", width = 800, height = 600, res = 100)
ggplot(lalonde, aes(x = re78, fill = factor(treat))) +
  geom_histogram(alpha = 0.6, bins = 30, position = "identity") +
  scale_fill_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                   labels = c("对照组", "处理组")) +
  labs(title = "LaLonde 数据：收入分布直方图",
       x = "1978 年真实收入 ($)",
       y = "频数",
       fill = "组别") +
  theme_minimal(base_size = 14) +
  theme(legend.position = "bottom")
dev.off()
cat("已生成: 02_histogram_comparison.png\n")

# 图3: FRT 置换分布直方图
png("R/figures/03_permutation_distribution.png", width = 800, height = 600, res = 100)
par(mar = c(5, 5, 4, 2))
hist(perm_tauhat, breaks = 50, col = "steelblue", border = "white",
     main = "FRT 置换分布 (B=10,000)",
     xlab = "置换后的差值均值 ($)", ylab = "频数",
     cex.lab = 1.3, cex.main = 1.5)
abline(v = tauhat, col = "red", lwd = 3, lty = 1)
abline(v = -tauhat, col = "red", lwd = 3, lty = 2)
abline(v = 0, col = "black", lwd = 1, lty = 3)
legend("topright", c(paste("观测值:", round(tauhat, 2)),
                     paste("p值:", round(p_value, 4))),
       col = c("red", "red"), lty = c(1, 2), lwd = c(2, 2), cex = 1.2)
dev.off()
cat("已生成: 03_permutation_distribution.png\n")

# 图4: 累积分布函数 (CDF) 比较 - KS 检验可视化
png("R/figures/04_cdf_comparison.png", width = 800, height = 600, res = 100)
par(mar = c(5, 5, 4, 2))
treatment_ecdf <- ecdf(treatment_y)
control_ecdf <- ecdf(control_y)
all_y <- sort(unique(c(treatment_y, control_y)))

# 使用 base R 画 CDF
plot(control_ecdf, col = "#3498db", lwd = 2, lty = 2,
     main = "CDF 比较 - KS 检验", xlab = "1978 年真实收入 ($)", ylab = "累积概率",
     cex.lab = 1.3, cex.main = 1.5)
plot(treatment_ecdf, col = "#e74c3c", lwd = 2, lty = 1, add = TRUE)
legend("bottomright", c("对照组 (虚线)", "处理组 (实线)"),
       col = c("#3498db", "#e74c3c"), lty = c(2, 1), lwd = 2, cex = 1.2)
mtext(paste("KS 统计量 D =", round(D, 4)), side = 3, line = 0.5, cex = 1.1)
dev.off()
cat("已生成: 04_cdf_comparison.png\n")

# 图5: 密度估计比较
png("R/figures/05_density_comparison.png", width = 800, height = 600, res = 100)
ggplot(lalonde, aes(x = re78, fill = factor(treat), color = factor(treat))) +
  geom_density(alpha = 0.3, linewidth = 1.5) +
  scale_fill_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                    labels = c("对照组", "处理组")) +
  scale_color_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                    labels = c("对照组", "处理组")) +
  labs(title = "LaLonde 数据：收入核密度估计",
       x = "1978 年真实收入 ($)",
       y = "密度",
       fill = "组别", color = "组别") +
  theme_minimal(base_size = 14) +
  theme(legend.position = "bottom")
dev.off()
cat("已生成: 05_density_comparison.png\n")

# 图6: Q-Q 图 - 检验正态性
png("R/figures/06_qq_comparison.png", width = 800, height = 400, res = 100)
par(mfrow = c(1, 2), mar = c(4, 4, 3, 2))
qqnorm(treatment_y, main = "处理组 Q-Q 图", cex.main = 1.3)
qqline(treatment_y, col = "red", lwd = 2)
qqnorm(control_y, main = "对照组 Q-Q 图", cex.main = 1.3)
qqline(control_y, col = "red", lwd = 2)
dev.off()
cat("已生成: 06_qq_comparison.png\n")

cat("\n所有图表生成完成！\n")
