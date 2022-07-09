# Bitcoin Arbitrage

This is a Jupyter notebook that reads in two data sheets ('bitstamp and coinbase'), checks them for errors and other bad data (and corrects those errors), and then analyzes the data to see if there is an arbitrage possibility within the data set where a profit could be made. If a possible profit exists we will also document that and graph the results to a table.

---

## Technologies

This project utilizes JupyterLab 3.3.2 and Pandas 1.4.2 and Matplotlib 4.0:

* [JupyterLab](https://jupyter.org/) - For the notebook creation and running of the code.

* [pandas](https://github.com/pandas-dev/pandas/blob/main/README.md) - For reading the csv files.

* [Matplotlib](https://matplotlib.org/) - For plotting graphs and charts that appear below the code.

---

## Installation Guide

Before running this notebook you will want to make sure you have JupyterLab and Pandas installed. To do this check to see that they are on your system.

```python

    conda list pandas
    
    conda list jupyterlab
```

Make sure that both of these show in your system before proceeding.

---

## Usage

To use the bitcoin arbitrage notebook, begin by typing jupyter lab in your terminal. Next, find the folder with the notebook(crypto_arbitrage.ipynb) and double click it to open it up in a new launcher. Then, begin running through each section of the application to get the appropriate data.

```python
jupyter lab
```

Once in the notebook it will take you through a step-by-step process as it Collects the Data, Prepares the Data, and Analyzes the Data.
You will be granted visualizations along the way to help better see and understand the data.

We do believe everything is thoroughly explained in the notebook, but please let us know if you have any further questions.

---
## Contributors

### Matthew Stream
m.stream3663@gmail.com

[LinkedIn](https://www.linkedin.com/in/matthew-stream-mba-215634102/)

---

## License

MIT
