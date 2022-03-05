# neuron network understanding and visualizing


## Introduction

this depository contain many fun topic about neuron network understanding and visualizing. the topic are as follows:

* the visualization of filter and classification score.
* human attack
* style transfer

next i will briefly introduce these topic.

#### visualizing of filters

we can divided this topic into two situation.

***1. given no image***, what kind of pattern CNN's filter is trying to catch? and what is the definition of cat (a classification category) in CNN's mind?

**2. given a input image**, we need to answer these two question: which pixel of the image maximize the activation of filter? which part of the image is important to the classification score?

#### human attack

human attack's  goal is: given a image(eg. a image of cat) , we are trying to fool the CNN to mistaking the cat as a dog or other classes. 

#### style transfer

this topic can be divided into ***feature inversion*** and ***texture synthesis***.

feature inversion's goal is: given a image, we try to reconstruct the input image from CNN layers output.
texture synthesis's goal is: given an input texture image, we try to extract the texture information from the GRAM matrix computed from CNN layers output.

the method we use for these topic is ***Gradient Ascent***. and some tricks we use for generating nicer output are as follows:

## Keywords

*Gradient Ascent*, *Gram matrix*, *Saliency map*, *model attack*, *feature inversion*, *texture synthesis*, *style transfer*

## Result

* filter and class visualization

| layer num | result |
| ------- | ----- |
| input   |       |
| layer1   |       |
| layer2   |       |
| layer3   |       |
| layer4   |       |
| class   |       |

* saliency map for class score and filter

| layer num | result |
| ------- | ----- |
| input   |       |
| layer1   |       |
| layer2   |       |
| layer3   |       |
| layer4   |       |
| class   |       |
* human attack

| origin | result | difference  |
| ------- | ----- | ---- |
| ![]()   |       |      |

* feature inversion

| layer num | result |
| ------- | ----- |
| input   |       |
| layer1   |       |
| layer2   |       |
| layer3   |       |
| layer4   |       |
| class   |       |


* texture synthesis

| layer num | result |
| ------- | ----- |
| input   |       |
| layer1   |       |
| layer2   |       |
| layer3   |       |
| layer4   |       |
| class   |       |

* style transfer

| content | style | result |
| ------- | ----- | ---- |
| ![]()   |       |      |



## Reference