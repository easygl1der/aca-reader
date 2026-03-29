# Chi-square distribution for variance CI illustration
# df = n-1 degrees of freedom, here n = 20, df = 19

library ggplot2

df <- 19
alpha <- 0.05

# Critical values
chi_lower <- qchisq(1 - alpha/2, df)  # chi^2_{1-alpha/2, df}
chi_upper <- qchisq(alpha/2, df)      # chi^2_{alpha/2, df}

# Create data for plotting
x <- seq(0, 50, length.out = 1000)
y <- dchisq(x, df)

# Create dataframe
plot_data <- data.frame(x = x, y = y)

# Shade the rejection regions
p <- ggplot(plot_data, aes(x = x, y = y)) +
  geom_line(color = "black", linewidth = 1) +
  # Lower tail (left rejection region)
  stat_function(
    fun = function(x) dchisq(x, df),
    xlim = c(0, chi_lower),
    geom = "area",
    fill = "#FF6B6B", alpha = 0.6
  ) +
  # Upper tail (right rejection region)
  stat_function(
    fun = function(x) dchisq(x, df),
    xlim = c(chi_upper, 50),
    geom = "area",
    fill = "#FF6B6B", alpha = 0.6
  ) +
  # Confidence interval region
  stat_function(
    fun = function(x) dchisq(x, df),
    xlim = c(chi_lower, chi_upper),
    geom = "area",
    fill = "#4ECDC4", alpha = 0.5
  ) +
  # Vertical lines at critical values
  geom_vline(xintercept = chi_lower, linetype = "dashed", color = "#2C3E50", linewidth = 0.8) +
  geom_vline(xintercept = chi_upper, linetype = "dashed", color = "#2C3E50", linewidth = 0.8) +
  # Annotations
  annotate("text", x = chi_lower, y = max(y)*0.3,
           label = paste0("chi^2[1-alpha/2,", df,"] == ", round(chi_lower, 2)),
           parse = TRUE, vjust = -0.5, hjust = 1.2, size = 4) +
  annotate("text", x = chi_upper, y = max(y)*0.3,
           label = paste0("chi^2[alpha/2,", df,"] == ", round(chi_upper, 2)),
           parse = TRUE, vjust = -0.5, hjust = -0.2, size = 4) +
  # Labels for regions
  annotate("text", x = 8, y = max(y)*0.9, label = "Rejection\n(alpha/2)", size = 3.5, color = "#C0392B") +
  annotate("text", x = 38, y = max(y)*0.9, label = "Rejection\n(alpha/2)", size = 3.5, color = "#C0392B") +
  annotate("text", x = 23, y = max(y)*0.7, label = "Confidence\nRegion", size = 3.5, color = "#16A085") +
  # Labs
  labs(
    title = expression(paste("Chi-square Distribution ", chi^2, "(", df, ")")),
    x = expression(paste(chi^2, " value")),
    y = "Density"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(hjust = 0.5, face = "bold"),
    panel.grid.minor = element_blank()
  ) +
  xlim(0, 50)

# Save
ggsave("chi-square-ci.pdf", plot = p, width = 8, height = 5, dpi = 300)
ggsave("chi-square-ci.png", plot = p, width = 8, height = 5, dpi = 300)

cat("Plot saved: chi-square-ci.png\n")
cat(sprintf("df = %d, alpha = %.2f\n", df, alpha))
cat(sprintf("chi_lower (1-alpha/2) = %.4f\n", chi_lower))
cat(sprintf("chi_upper (alpha/2) = %.4f\n", chi_upper))
