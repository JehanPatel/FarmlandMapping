
![Downloads](https://img.shields.io/github/downloads/JehanPatel/FarmlandMapping/total) ![Contributors](https://img.shields.io/github/contributors/JehanPatel/FarmlandMapping?color=dark-green) ![Forks](https://img.shields.io/github/forks/JehanPatel/FarmlandMapping?style=social) ![Stargazers](https://img.shields.io/github/stars/JehanPatel/FarmlandMapping?style=social) ![Issues](https://img.shields.io/github/issues/JehanPatel/FarmlandMapping) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Details About the Project](#Details-About-The-Project)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Authors](#authors)

## About The Project

The objective of our project is to make a farmland mapping project which will take location data from users using a website. Then using that data, we will get soil pictures using maps and
district names. Then using different data sets we can display the common crops grown there and also give them a few unique rare grown crops suitable for their location and soil type and rainfall type and such. We also aim to provide them links to articles and videos on how to grow such crops effectively. In order to make the application more practical and useful, we also aim to add language translation into our page so that all the necessary information can be translated into the local languages for easy understanding. So in the end, the user receives practical info on which they can earn more. Farmers often lack the resources and knowledge to understand what different and more profitable crops to grow based on their soil and weather conditions. They usually follow the common trend and grow crops accordingly without taking into consideration what’s good for them and their land in the long run. So our solution provides those practical insights and helps the user in understanding the need and process to grow different crops and increase their profits and efficiency.

## Details About The Project

# Frontend:

● Capture Coordinates:
Using here maps javascript API to capture the coordinates of the map with appropriate zoom and utilizing javascript to determine the width and height ofthe captured area. Here Maps JavaScript API: Integrate the Here Maps JavaScript API to display satellite maps on the website and enable interactive functionalities.

● Location Search API: This maps location search API enables users to easily search for desired areas on the map.

● Map Area Selection: Develop functionality allowing users to delineate a farmland area on the map using four markers to form a rectangle.

● Soil Image Upload: Implement a feature enabling users to directly upload soil images for analysis.

# Backend

● Web Server: Utilize Flask, a color matching against known soil color requests and responses.

● Coordinate capture: We collect four coordinates to determine a bounding box, then calculate the centroid. This centroid, along with width, height, and zoom level, is used in a

● REST API request to download the corresponding image of the selected area.

● Dominant Color Extraction: Develop backend processes to extract the dominant color from the captured or uploaded images.

● Closest Soil Color Match: Calculate the Euclidean distance between the RGB (Red, green, and blue) values of the dominant color and predefined soil colors to determine the closest match.

● Output Display: Display the closest matched soil color on the website interface.

● User Interface: Design an intuitive and user-friendly interface for displaying maps, enabling area selection, uploading soil images, and presenting the results of soil color matching.

● Bhashini API: We will utilize Bhashini API to translate our web page into various different regional languages for ease of understanding for the farmers.

● Optimization and Performance: Implement optimization strategies to ensure efficient processing and response times. Consider implementing caching mechanisms for frequently accessed data to enhance overall system performance.

● Testing and Validation: Conduct comprehensive testing to ensure the reliability, accuracy, and functionality of the system. It helps validate the accuracy of soil color matching against known soil color references.

## Roadmap

See the [open issues](https://github.com/JehanPatel/FarmlandMapping/issues) for a list of proposed features (and known issues).
Please have a look at our [Report](https://github.com/JehanPatel/FarmlandMapping/blob/main/Group_071_21BCE10551_Phase%202_Final%20Report.pdf) for the complete flow and details of our project.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/JehanPatel/FarmlandMapping/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/JehanPatel/FarmlandMapping/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

## Authors

* **Jehan Patel** - [Jehan Patel](https://github.com/JehanPatel)
* **Neel Jain** - [Jehan Patel](https://github.com/Neel-2002)
* **Abhinav** - [Jehan Patel](https://github.com/Abhinav4291)
* **Akash** - [Jehan Patel](https://github.com/akashgithub427)
* **Rakshit Pandey** - [Jehan Patel](https://github.com/rakshit1104)

