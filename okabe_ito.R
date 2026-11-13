# Okabe-Ito (Wong) colorblind-safe palette for base R and ggplot2.
# Base R 4.0+ also has palette.colors(palette = "Okabe-Ito"), which starts with
# black and adds gray as a ninth color.

okabe_ito <- c(
  orange = "#E69F00", sky_blue = "#56B4E9", bluish_green = "#009E73",
  yellow = "#F0E442", blue = "#0072B2", vermillion = "#D55E00",
  reddish_purple = "#CC79A7", black = "#000000"
)

# Recommended order when a figure has fewer than eight groups (yellow last).
okabe_ito_order <- unname(okabe_ito[c("orange", "blue", "bluish_green", "vermillion",
                                      "sky_blue", "reddish_purple", "black", "yellow")])

# ggplot2:
#   ggplot(df, aes(x, y, colour = group)) + geom_point() +
#     scale_colour_manual(values = okabe_ito_order)
#   ... + scale_fill_manual(values = okabe_ito_order)

# Base R:
#   palette(okabe_ito_order)
#   plot(x, y, col = as.integer(group), pch = 19)
