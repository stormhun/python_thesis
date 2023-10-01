
# UWIN Database Parser and visualizer 



## Installation

1. Clone the project repository to your local machine using Git:

   ```bash
   git clone https://github.com/stormhun/python_thesis.git
   ```

   .

2. Navigate to the project directory:

   ```bash
   cd python-thesis
   ```

3. Install project dependencies using `pip` and the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all the required Python packages listed in the `requirements.txt` file.

## Usage

Now that you have installed the required dependencies, you can proceed to use the project as intended.

To read in an occupancy report from the uwin DB run the commmand
   ```bash
    python csvparser.py your-occupancy-report-name.csv --start-date mm/dd/yyyy
```
    ` if you don't specify a start date we will use the default 1/1/2022 `

This will generate list of sites from the csv and save it to a binary file named **tst.pickle** this way you don't have to parse in the file each time.

You can then run the **loadindemo.py** file to generate plots for each site

```bash 
python loadindemo.py
```

## Result

![Sample Plot for Powell Butte ](https://github.com/stormhun/python_thesis/blob/main/Powell%20Butte%201.jpg)


There are other plotting options but they are not quite as polished as the `plot_all_sites` method

