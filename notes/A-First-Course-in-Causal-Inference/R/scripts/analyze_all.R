library(Matching)
library(ggplot2)
library(dplyr)
library(sandwich)
library(lmtest)

data(lalonde)

# Extract variables
z <- lalonde$treat
y <- lalonde$re78
n1 <- sum(z)
n0 <- length(z) - n1
n <- length(z)

cat("=== Generating Ultra High-Resolution Figures ===\n")

# Descriptive statistics
treatment <- lalonde[lalonde$treat == 1, ]
control <- lalonde[lalonde$treat == 0, ]

# FRT test statistics
tauhat <- mean(y[z == 1]) - mean(y[z == 0])
s1_sq <- var(y[z == 1])
s0_sq <- var(y[z == 0])
treatment_y <- y[z == 1]
control_y <- y[z == 0]
ks_result <- ks.test(treatment_y, control_y)
D <- ks_result$statistic

# Permutation test
set.seed(42)
B <- 10000
perm_tauhat <- numeric(B)
for (b in 1:B) {
  z_perm <- sample(z)
  perm_tauhat[b] <- mean(y[z_perm == 1]) - mean(y[z_perm == 0])
}
p_value <- mean(abs(perm_tauhat) >= abs(tauhat))

# Create figures directory
dir.create("R/figures", showWarnings = FALSE)

# Ultra high resolution: DPI = 600, width = 12 inches
dpi <- 600
width <- 12
height <- 8

# Common theme for all plots
base_theme <- theme_minimal(base_size = 20) +
  theme(legend.position = "bottom",
        plot.title = element_text(hjust = 0.5, size = 22),
        axis.title = element_text(size = 18),
        axis.text = element_text(size = 14),
        legend.text = element_text(size = 16))

# Figure 1: Boxplot
png("R/figures/01_boxplot_comparison.png", width = width * dpi, height = height * dpi, res = dpi)
print(ggplot(lalonde, aes(x = factor(treat), y = re78, fill = factor(treat))) +
  geom_boxplot(outlier.size = 3, linewidth = 1.5) +
  scale_fill_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                   labels = c("Control", "Treatment")) +
  labs(title = "LaLonde Data: Treatment vs Control Income Comparison",
       x = "Group (0=Control, 1=Treatment)",
       y = "Real Earnings in 1978 ($)",
       fill = "Group") +
  base_theme)
dev.off()
cat("Generated: 01_boxplot_comparison.png\n")

# Figure 2: Histogram
png("R/figures/02_histogram_comparison.png", width = width * dpi, height = height * dpi, res = dpi)
print(ggplot(lalonde, aes(x = re78, fill = factor(treat))) +
  geom_histogram(alpha = 0.6, bins = 50, position = "identity", linewidth = 0.8) +
  scale_fill_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                   labels = c("Control", "Treatment")) +
  labs(title = "LaLonde Data: Income Distribution Histogram",
       x = "Real Earnings in 1978 ($)",
       y = "Frequency",
       fill = "Group") +
  base_theme)
dev.off()
cat("Generated: 02_histogram_comparison.png\n")

# Figure 3: Permutation distribution
png("R/figures/03_permutation_distribution.png", width = width * dpi, height = height * dpi, res = dpi)
par(mar = c(8, 8, 6, 2), cex.lab = 1.8, cex.main = 2, cex.axis = 1.5)
hist(perm_tauhat, breaks = 70, col = "steelblue", border = "white",
     main = "FRT Permutation Distribution (B=10,000)",
     xlab = "Permuted Difference-in-Means ($)", ylab = "Frequency")
abline(v = tauhat, col = "red", lwd = 4, lty = 1)
abline(v = -tauhat, col = "red", lwd = 4, lty = 2)
abline(v = 0, col = "black", lwd = 2, lty = 3)
legend("topright", c(paste("Observed:", round(tauhat, 2)),
                     paste("p-value:", round(p_value, 4))),
       col = c("red", "red"), lty = c(1, 2), lwd = c(3, 3), cex = 1.5)
dev.off()
cat("Generated: 03_permutation_distribution.png\n")

# Figure 4: CDF comparison
png("R/figures/04_cdf_comparison.png", width = width * dpi, height = height * dpi, res = dpi)
par(mar = c(8, 8, 6, 2), cex.lab = 1.8, cex.main = 2, cex.axis = 1.5)
treatment_ecdf <- ecdf(treatment_y)
control_ecdf <- ecdf(control_y)

plot(control_ecdf, col = "#3498db", lwd = 3, lty = 2,
     main = "CDF Comparison - KS Test", xlab = "Real Earnings in 1978 ($)", ylab = "Cumulative Probability")
plot(treatment_ecdf, col = "#e74c3c", lwd = 3, lty = 1, add = TRUE)
legend("bottomright", c("Control (dashed)", "Treatment (solid)"),
       col = c("#3498db", "#e74c3c"), lty = c(2, 1), lwd = 3, cex = 1.5)
mtext(paste("KS Statistic D =", round(D, 4)), side = 3, line = 0.5, cex = 1.6)
dev.off()
cat("Generated: 04_cdf_comparison.png\n")

# Figure 5: Density comparison
png("R/figures/05_density_comparison.png", width = width * dpi, height = height * dpi, res = dpi)
print(ggplot(lalonde, aes(x = re78, fill = factor(treat), color = factor(treat))) +
  geom_density(alpha = 0.3, linewidth = 2) +
  scale_fill_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                    labels = c("Control", "Treatment")) +
  scale_color_manual(values = c("0" = "#3498db", "1" = "#e74c3c"),
                    labels = c("Control", "Treatment")) +
  labs(title = "LaLonde Data: Income Kernel Density Estimation",
       x = "Real Earnings in 1978 ($)",
       y = "Density",
       fill = "Group", color = "Group") +
  base_theme)
dev.off()
cat("Generated: 05_density_comparison.png\n")

# Figure 6: Q-Q plot
png("R/figures/06_qq_comparison.png", width = width * dpi, height = height * dpi / 2, res = dpi)
par(mfrow = c(1, 2), mar = c(6, 6, 4, 2), cex.lab = 1.5, cex.main = 1.6, cex.axis = 1.3)
qqnorm(treatment_y, main = "Treatment Group Q-Q Plot", xlab = "Theoretical Quantiles", ylab = "Sample Quantiles", qqline.args = list(col = "red", lwd = 3))
qqline(treatment_y, col = "red", lwd = 3)
qqnorm(control_y, main = "Control Group Q-Q Plot", xlab = "Theoretical Quantiles", ylab = "Sample Quantiles", qqline.args = list(col = "red", lwd = 3))
qqline(control_y, col = "red", lwd = 3)
dev.off()
cat("Generated: 06_qq_comparison.png\n")

cat("\nAll ultra high-resolution figures generated successfully!\n")
