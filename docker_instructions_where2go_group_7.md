# COLX 523: Group 7 Project - where2go

## Members: Sheena Salwan, Shounak Mondal, Quang Vu, Toni Li

## Peer review instructions

### Steps to download and run docker image

**Prerequisites**: Docker should be running

-   Download 'colx\_523\_group\_7.tar'

-   Load the docker image, run the command: `docker load < colx_523_group_7.tar` Once the image is successfully loaded, you will see a message `Loaded image: colx_523_group_7:latest`

-   Run the docker image with command: `docker run -p 9999:9999 colx_523_group_7`

    **Note: The external port used here is 9999**

-   Go to browser (chrome recommended) and type: `localhost:9999` .Project page should load successfully.

### Project Interface- Start Exploring

There are mainly 3 parts of the interface:

-   **where2go Project Introduction Video -** Check our introduction video! It will explain our project, our methodologies and the future of the project in less than 90 seconds!

-   **Corpus Statistics -** This shows statistics about our corpus and the word cloud.

-   **Corpus Search -** You can either-

    -   Search a text directly in the corpus using **Search Text in Corpus**. This will search the text within the overview description in our corpus.

    -   Or Choose from a list of Annotations provided by human annotators ,using **Search Annotations in Corpus**. This will show results that match a particular annotation.

        **Here's how you can do it-**

        Are you an adventurous person who wants to explore different activities this summer? Type activity name in '**Search Text in Corpus'** for places that offer activities like **kayaking, swimming, snorkeling, riding or scooter.** You can also select from the drop down list in '**Search Annotations'** e.g choose **'hiking'** from the list.

        Or you may be a person who likes cooking. Select '**cooking**' from the drop down list in '**Search Annotations**' and find out places that offer cooking classes

        Or you might be a person who loves to be close to nature. Select '**walking tour'** from the drop down list in '**Search Annotations**' to search for some walking tours.

    Whatever your interest may be, you can search easily on where2go. Happy Exploring!
