from Pardee_Package import color_palletes as pardee_colors
from Pardee_Package import style_dictionaries as pardee_styles


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def sinplot(flip=1):
    fig = plt.figure()
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
        
def test_crimson():
    color = pardee_colors.crimson_color_gradient()
    style = pardee_styles.standard_style
    sns.set_style(style)
    sns.set_palette(color)
    sinplot()
    plt.title("Testing Crimson Colors")
    
def test_DU():
    color = pardee_colors.DU_color_pallete()
    style = pardee_styles.standard_style
    sns.set_style(style)
    sns.set_palette(color)
    sinplot()
    plt.title("Testing DU Colors")
    
def test_gold():
    color = pardee_colors.gold_color_gradient()
    style = pardee_styles.standard_style
    sns.set_style(style)
    sns.set_palette(color)
    sinplot()
    plt.title("Testing Gold Colors")
    
def test_colorblind():
    color = pardee_colors.color_blind_friendly_color_pallete()
    style = pardee_styles.standard_style
    sns.set_style(style)
    sns.set_palette(color)
    sinplot()
    plt.title("Testing Colorblind Colors")
    
def test_grayscale():
    color = pardee_colors.grayscale_color_pallete()
    style = pardee_styles.grayscale_style
    sns.set_style(style)
    sns.set_palette(color)
    sinplot()
    plt.title("Testing Grayscale")
    
def test_colorblind_contrast():
    color = pardee_colors.high_contrast_color_blind_pallete()
    style = pardee_styles.standard_style
    sns.set_style(style)
    sns.set_palette(color)
    sinplot()
    plt.title("Testing contrasting colorblind")
    
def test_contrast():
    color = pardee_colors.high_contrast_color_pallete()
    style = pardee_styles.standard_style
    sns.set_style(style)
    sns.set_palette(color)
    sinplot()
    plt.title("Testing high contrast")
    
def test_colors():
    test_DU()
    test_crimson()
    test_gold()
    test_colorblind()
    test_grayscale()
    test_colorblind_contrast()
    test_contrast()
    
test_colors()