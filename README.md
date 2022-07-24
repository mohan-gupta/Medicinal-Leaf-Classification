<img src = "https://github.com/mohan-gupta/Medicinal-Leaf-Classification/blob/main/artifacts/MLC.gif"> <br>

# Medicinal Leaf Classification

Mother earth is enriched and nourished with a variety of plants. These plants are useful in many ways such as drug formulation, production of herbal products, and medicines to cure many common ailments and diseases. For the past 5000 years, Ayurveda, a traditional Indian medicinal system is widely accepted even today. India is a rich country for being the habitat for a variety of medicinal plants. Many parts of the plants such as leaves, bark, root, seeds, fruits, and many more are used as a vital ingredient for the production of herbal medicines.
# Objective

Herbal medicines are preferred in both developing and developed countries as an alternative to synthetic drugs mainly because of no side effects. Recognition of these plants by human sight will be tedious, time-consuming, and inaccurate. Applications of image processing and computer vision techniques for the identification of the medicinal plants are very crucial as many of them are under extinction as per the IUCN records. Hence, the digitization of useful medicinal plants is crucial for the conservation of biodiversity.

Dataset Link: [Medicinal Leaf data from Mendeley Data](https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/nnytj2v3n5-1.zip)

# Approach

- Applied data scaling to scale the pixels within the range [0-1]. 
- Applied Following data Augmentations:
   1. Random Flip - Both horizontal and vertical.
   2. Random Rotation - By a factor of 0.2.
   3. Random Zoom - with height factor 0.2 and width factor 0.3. 

- Used Pre-Trained ResNet50-V2 as base model.

<img src = "https://github.com/mohan-gupta/Medicinal-Leaf-Classification/blob/main/artifacts/ResNet%20V2%20skip%20connection.png"> <br>

- Froze the layers of the base model.
- Added softmax layer to the base model (trainable layer).
- Used Reduce LR on Plateau callback for training.
- Trained for 15 Epochs.
- Used Streamlit for the User Interface.

# Results Obtained

### Confusion Matrix
<img src = "https://github.com/mohan-gupta/Medicinal-Leaf-Classification/blob/main/artifacts/confusion_matrix.png"> <br>

### Classification Report

                precision    recall  f1-score   support

           0       1.00      0.82      0.90        11
           1       0.96      1.00      0.98        24
           2       1.00      1.00      1.00         7
           3       1.00      1.00      1.00         8
           4       0.92      1.00      0.96        22
           5       1.00      1.00      1.00         8
           6       0.92      0.96      0.94        24
           7       1.00      1.00      1.00        11
           8       1.00      0.87      0.93        15
           9       1.00      1.00      1.00        16
          10       0.75      1.00      0.86         3
          11       0.87      0.93      0.90        14
          12       0.85      0.92      0.88        12
          13       1.00      1.00      1.00        18
          14       0.87      0.81      0.84        16
          15       1.00      1.00      1.00         8
          16       1.00      1.00      1.00        14
          17       0.90      0.75      0.82        12
          18       1.00      1.00      1.00        10
          19       1.00      0.90      0.95        10
          20       0.88      0.88      0.88         8
          21       1.00      1.00      1.00        11
          22       0.94      1.00      0.97        16
          23       1.00      1.00      1.00         9
          24       1.00      0.94      0.97        16
          25       0.90      1.00      0.95         9
          26       0.86      1.00      0.92         6
          27       0.92      1.00      0.96        11
          28       1.00      0.83      0.91        12
          29       0.83      0.83      0.83         6

    accuracy                           0.95       367
    macro avg       0.94     0.95      0.94       367
    weighted avg    0.95     0.95      0.95       367

### ROC-AUC Curve
<img src = "https://github.com/mohan-gupta/Medicinal-Leaf-Classification/blob/main/artifacts/roc_curve.png"> <br>
