<h1><B>STYLE TRANSFER</B></h1>

# Introduction:

Neural networks had got an emmense popularity due to their never ending scope. Here, I have presented the code work of <a href = "https://arxiv.org/abs/1508.06576">Style Transfer</a> Paper.
The basic idea behind style tranfer is that it takes the style of an image and merges it with the contents of other image. As a result, we get a
combination of two images.

# My Work:
Here, I am represting the vode work of Style tranfer paper as well as the different outputs got after changing the hyperparameters (here, the Style loss
Weight and the Content loss weight). The total number of EPOCHS was kept fixed at 1000. In one of the case, I changed the total nber of epochs to 100 (as shown in the table below). 

# Files and Folders Introduction:
1. <B>Style_transfer.py</B> is the main file having python code of style transfers from scratch based on the Style Transfer paper.
2. <B>Style_transfers-using_tensorflow_power.py</B>, this file is based on implementation of Style Transfer based on inbuilt Tensorflow Modules 
and functions.
3. <B>sample_image</B> - This folder has images which we took as sample or the images on which we applied the style of other images.
4. <B>style_images</B> - This folder has images which we took as Style imaegs. That is the imaegs from whch we borrow the styles.
5. <B>combinaions</B> - this is the folder containing the pairs of style images and content images used.
6. <B>results</B> - this folder contains the final results obtained after combining the images as present in combinations under different conditions.

# Model Used:

<img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/model.png" height = '1400' width = '800'/>

# Final Output:
<table>
  <tr>
    <td>
      Combinations
    </td>
    <td>
      Results
    </td>
    <td>
      Conditions
    </td>
  <tr>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/combinations/combo_1.png"/>
    </td>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/results/combination_1.png", align = "right"/>
    </td>
    <td>
      Total Number of Epochs = 100<br>
      Style Loss Weight = 10e-4<br>
      Content Loss Weight = 10e-2<br>
  </tr>
  <tr>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/combinations/combo_1.png"/>
    </td>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/results/combination_1000-epochs.png"/>
    </td>
    <td>
      Total Number of Epochs = 1000<br>
      Style Loss Weight = 10e-4<br>
      Content Loss Weight = 10e-2<br>
    </td>
  </tr>
  <tr>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/combinations/combo_2.png"/>
    </td>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/results/combination_1000_para_1_epochs.png"/>
    </td>
    <td>
       Total Number of Epochs = 1000<br>
       Style Loss Weight = 10e-2<br>
       Content Loss Weight = 10e-1<br>
    <td>
  </tr>
  <tr>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/combinations/combo_2.png"/>
    </td>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/results/combination_1000_para_epochs.png"/>
    </td>
    <td>
       Total Number of Epochs = 1000<br>
       Style Loss Weight = 10e-4<br>
       Content Loss Weight = 1<br>
    </td>
  </tr>
  <tr>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/combinations/combo_2.png"/>
    </td>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/results/combination_2_%201000.png"/>
    </td>
    <td>
       Total Number of Epochs = 1000<br>
       Style Loss Weight = 10e-4<br>
       Content Loss Weight = 10e-2<br>
    </td>
  </tr>
  <tr>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/combinations/combo_3.png"/>
    </td>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/results/combination_3_%201000.png.png"/>
    </td>
    <td>
       Total Number of Epochs = 1000<br>
       Style Loss Weight = 10e-4<br>
       Content Loss Weight = 10e-2<br>
    </td>
  </tr>
  <tr>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/combinations/combo_4.png"/>
    </td>
    <td>
      <img src = "https://github.com/AYUSH-ISHAN/Style_Transfer/blob/main/results/combination_4.png"/>
    </td>
    <td>
       Total Number of Epochs = 1000<br>
       Style Loss Weight = 10e-4<br>
       Content Loss Weight = 10e-2<br>
    </td>
  </tr>
</table>

