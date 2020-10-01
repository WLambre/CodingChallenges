Given a csv file, with information in the following structure

| Food  | Attribute |
| ------------- | ------------- |
| Apple  | Fruit  |
| Carrot  | Vegetable  |
| Spinach  | Vegetable  |
| Spinach  | Leafy Green  |
| Carrot  | Root  |
| Apple  | Sweet  |
| Apple  | Cider  |
| Apple  | Tree  |
| Carrot  | Vitamin K  |
| Spinach  | Flowers |
| Spinach  | Iron |


Rearrange it to be flat, as follows

| Food  | Attribute 1 | Attribute 2 | Attribute 3 | Attribute 4 |
| ------------- | ------------- |
| Apple  | Fruit  | Sweet  | Tree  | Cider  |
| Carrot  | Vegetable  | Root  | Vitamin K  |  |
| Spinach  | Vegetable  | Leafy Green  | Flowers | Iron |

The following string is the initial date to be used:

Food,Attribute
Apple,Fruit
Carrot,Vegetable
Spinach,Vegetable
Spinach,Leafy Green
Carrot,Root
Apple,Sweet
Apple,Cider
Apple,Tree
Carrot,Vitamin K
Spinach,Flowers
Spinach,Iron
