# Medicinal Leaf Classification
<img src = "artifacts/medicinal leaf.gif"> <br>

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

<img src = "artifacts/ResNet%20V2%20skip%20connection.png"> <br>

- Froze the layers of the base model.
- Added softmax layer to the base model (trainable layer).
- Used Reduce LR on Plateau callback for training.
- Trained for 20 Epochs.
- Used Streamlit for the User Interface.

# Results Obtained

### Confusion Matrix
<img src = "artifacts/confusion matrix.jpg"> <br>

### Classification Report

                precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       0.95      1.00      0.98        20
           2       0.81      1.00      0.90        13
           3       1.00      1.00      1.00        11
           4       0.93      1.00      0.97        14
           5       1.00      1.00      1.00         9
           6       0.93      1.00      0.96        13
           7       1.00      1.00      1.00         8
           8       1.00      0.78      0.88         9
           9       1.00      1.00      1.00        15
          10       1.00      1.00      1.00         8
          11       0.93      1.00      0.97        14
          12       0.92      1.00      0.96        12
          13       1.00      1.00      1.00        16
          14       1.00      0.93      0.97        15
          15       1.00      1.00      1.00        14
          16       1.00      1.00      1.00        11
          17       0.74      0.93      0.82        15
          18       1.00      1.00      1.00         4
          19       1.00      1.00      1.00        12
          20       1.00      1.00      1.00         8
          21       1.00      0.89      0.94         9
          22       1.00      0.95      0.97        20
          23       1.00      1.00      1.00        14
          24       1.00      0.95      0.98        21
          25       1.00      1.00      1.00        13
          26       1.00      1.00      1.00         7
          27       1.00      0.74      0.85        19
          28       1.00      0.86      0.92         7
          29       1.00      1.00      1.00         6

    accuracy                           0.96       367
    macro avg       0.97      0.97      0.97       367
    weighted avg       0.97      0.96      0.96       367

### ROC-AUC Curve
<img src = "artifacts/roc-auc test.png"> <br>
