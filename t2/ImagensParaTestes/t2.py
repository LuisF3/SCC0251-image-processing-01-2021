#!/usr/bin/env python
# coding: utf-8

# # Trabalho 02 : realce e superresolução - 01/2021

# **Nome:** Luís Felipe Ribeiro Chaves
# 
# **NUSP:** 10801221
# 
# BCC/018

# Imports necessários no programa

# In[2]:


import numpy as np
import imageio

from matplotlib import pyplot as plt


# Leitura de parâmetros

# In[ ]:


bn = input()
hg = input()
fn = int(input())
gm = float(input())


# Leitura das imagens

# In[4]:


imgs = (
    imageio.imread(bn + '0.png'),
    imageio.imread(bn + '1.png'),
    imageio.imread(bn + '2.png'),
    imageio.imread(bn + '3.png')
)
ref_img_high = imageio.imread(hg)


# ## Realce de imagem

# In[6]:


def cumulative_hist(A, intensity_level):
    base = range(intensity_level)
    values = np.zeros(intensity_level)
    
    values[0] = np.sum(A == 0)
    for i in range(1, intensity_level):
        values[i] = values[i - 1] + np.sum(A == i)
        
    return (base, values)

def apply_hist_enhancement(img, hist):
    applied = ((len(hist[0]) - 1) / (img.shape[0] * img.shape[1])) * hist[1][img]
    mini = applied.min()
    maxi = applied.max()
    diff = maxi - mini
    return (applied - mini) * (img.shape[0] - 1) / diff

if fn == 0:
    imgs_enhc = imgs
elif fn == 1:
    ind_hists = (
        cumulative_hist(imgs[0], 256),
        cumulative_hist(imgs[1], 256),
        cumulative_hist(imgs[2], 256),
        cumulative_hist(imgs[3], 256)
    )
    imgs_enhc = (
        apply_hist_enhancement(imgs[0], ind_hists[0]),
        apply_hist_enhancement(imgs[1], ind_hists[1]),
        apply_hist_enhancement(imgs[2], ind_hists[2]),
        apply_hist_enhancement(imgs[3], ind_hists[3])
    )
elif fn == 2:
    img_concat = np.concatenate(imgs)
    conj_hists = cumulative_hist(img_concat, 256)
    
    imgs_enhc = (
        apply_hist_enhancement(imgs[0], conj_hists),
        apply_hist_enhancement(imgs[1], conj_hists),
        apply_hist_enhancement(imgs[2], conj_hists),
        apply_hist_enhancement(imgs[3], conj_hists)
    )
elif fn == 3:
    imgs_enhc = (
        255.0 * (imgs[0]/255.0) ** (1.0 / gm),
        255.0 * (imgs[1]/255.0) ** (1.0 / gm),
        255.0 * (imgs[2]/255.0) ** (1.0 / gm),
        255.0 * (imgs[3]/255.0) ** (1.0 / gm)
    )


# ## Superresolução

# In[9]:


sx, sy = imgs[0].shape
img_high = np.zeros((sx * 2, sy * 2))
for x in np.arange(sx):
    for y in np.arange(sy):
        bx, by = (x * 2, y * 2)
        img_high[bx    , by    ] = imgs_enhc[0][x, y]
        img_high[bx    , by + 1] = imgs_enhc[1][x, y]
        img_high[bx + 1, by    ] = imgs_enhc[2][x, y]
        img_high[bx + 1, by + 1] = imgs_enhc[3][x, y]


# ## Cálculo do erro

# In[8]:


n = img_high.shape[0]
rmse = 0

for i in range(n):
    for j in range(n):
        rmse += (img_high[i, j] - ref_img_high[i, j]) ** 2
        
rmse = np.sqrt(rmse/ (n ** 2))

print("%.4f" % rmse)

