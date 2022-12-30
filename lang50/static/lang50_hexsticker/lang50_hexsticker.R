# Create `lang50` hexsticker

library(ggplot2)
library(hexSticker)
library(showtext)
font_add_google("Ubuntu Mono")
showtext_auto()
p <- mtcars |> dplyr::filter(mpg > 35) |>
    ggplot(aes(x = mpg, y = wt)) +
    geom_point()
p <- p + theme_void() + theme_transparent()
sticker(
    p,
    package = "lang50",
    h_size = 1.5,
    h_color = "#337ab7",
    h_fill = "white",
    p_size = 40,
    p_y = 1,
    p_color = "#337ab7",
    p_family = "Ubuntu Mono",
    filename = "lang50_logo.png"
)
