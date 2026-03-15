library(Matching)
library(ggplot2)
library(dplyr)
library(sandwich)
library(lmtest)

data(lalonde)

cat("=== LaLonde Data Basic Info ===\n")
cat("Sample size:", nrow(lalonde), "\n")
cat("Treatment group:", sum(lalonde$treat), "\n")
cat("Control group:", nrow(lalonde) - sum(lalonde$treat), "\n\n")

treatment <- lalonde[lalonde$treat == 1, ]
control <- lalonde[lalonde$treat == 0, ]

cat("=== Treatment Group (re78) ===\n")
cat("Mean:", mean(treatment$re78), "\n")
cat("SD:", sd(treatment$re78), "\n")
cat("Median:", median(treatment$re78), "\n\n")

cat("=== Control Group (re78) ===\n")
cat("Mean:", mean(control$re78), "\n")
cat("SD:", sd(control$re78), "\n")
cat("Median:", median(control$re78), "\n\n")

z <- lalonde$treat
y <- lalonde$re78
n1 <- sum(z)
n0 <- length(z) - n1

tauhat <- mean(y[z == 1]) - mean(y[z == 0])
s1_sq <- var(y[z == 1])
s0_sq <- var(y[z == 0])
vhat <- s1_sq / n1 + s0_sq / n0
se <- sqrt(vhat)

cat("=== Neymanian Inference ===\n")
cat("Point estimate tauhat:", tauhat, "\n")
cat("Standard error:", se, "\n")
cat("95% CI: [", tauhat - 1.96*se, ",", tauhat + 1.96*se, "]\n")
cat("t statistic:", tauhat / se, "\n")
cat("p-value:", 2 * (1 - pnorm(abs(tauhat / se))), "\n\n")

model <- lm(re78 ~ treat, data = lalonde)
coef_default <- summary(model)$coefficients["treat", ]
coef_robust <- coeftest(model, vcov = vcovHC(model, type = "HC2"))["treat", ]

cat("=== OLS Comparison ===\n")
cat("OLS default - Estimate:", coef_default["Estimate"], ", SE:", coef_default["Std. Error"], "\n")
cat("OLS HC2 robust - Estimate:", coef_robust["Estimate"], ", SE:", coef_robust["Std. Error"], "\n")

dir.create("figures", showWarnings = FALSE)

# Boxplot
png("figures/boxplot_comparison.png", width = 800, height = 600, res = 100)
ggplot(lalonde, aes(x = factor(treat), y = re78, fill = factor(treat))) +
  geom_boxplot() +
  scale_fill_manual(values = c("0" = "lightblue", "1" = "lightcoral"),
                    labels = c("Control", "Treatment")) +
  labs(title = "LaLonde Data: Treatment vs Control Income Comparison",
       x = "Group (0=Control, 1=Treatment)",
       y = "Real Earnings in 1978 ($)",
       fill = "Group") +
  theme_minimal() +
  theme(legend.position = "bottom")
dev.off()

# Histogram
png("figures/histogram_comparison.png", width = 800, height = 600, res = 100)
ggplot(lalonde, aes(x = re78, fill = factor(treat))) +
  geom_histogram(alpha = 0.6, bins = 30, position = "identity") +
  scale_fill_manual(values = c("0" = "blue", "1" = "red"),
                    labels = c("Control", "Treatment")) +
  labs(title = "LaLonde Data: Income Distribution Histogram",
       x = "Real Earnings in 1978 ($)",
       y = "Frequency",
       fill = "Group") +
  theme_minimal() +
  theme(legend.position = "bottom")
dev.off()

cat("\nFigures saved to figures/ directory!\n")
