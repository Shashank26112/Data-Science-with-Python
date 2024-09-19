{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Bank Telemarketing Campaign Case Study."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this case study you’ll be learning Exploratory Data Analytics with the help of a case study on \"Bank marketing campaign\". This will enable you to understand why EDA is a most important step in the process of Machine Learning."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Problem Statement:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " \n",
    "\n",
    "The bank provides financial services/products such as savings accounts, current accounts, debit cards, etc. to its customers. In order to increase its overall revenue, the bank conducts various marketing campaigns for its financial products such as credit cards, term deposits, loans, etc. These campaigns are intended for the bank’s existing customers. However, the marketing campaigns need to be cost-efficient so that the bank not only increases their overall revenues but also the total profit. You need to apply your knowledge of EDA on the given dataset to analyse the patterns and provide inferences/solutions for the future marketing campaign.\n",
    "\n",
    "The bank conducted a telemarketing campaign for one of its financial products ‘Term Deposits’ to help foster long-term relationships with existing customers. The dataset contains information about all the customers who were contacted during a particular year to open term deposit accounts.\n",
    "\n",
    "\n",
    "**What is the term Deposit?**\n",
    "\n",
    "Term deposits also called fixed deposits, are the cash investments made for a specific time period ranging from 1 month to 5 years for predetermined fixed interest rates. The fixed interest rates offered for term deposits are higher than the regular interest rates for savings accounts. The customers receive the total amount (investment plus the interest) at the end of the maturity period. Also, the money can only be withdrawn at the end of the maturity period. Withdrawing money before that will result in an added penalty associated, and the customer will not receive any interest returns.\n",
    "\n",
    "Your target is to do end to end EDA on this bank telemarketing campaign data set to infer knowledge that where bank has to put more effort to improve it's positive response rate. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Importing the libraries."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the warnings.\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the useful libraries.\n",
    "import pandas as pd, numpy as np\n",
    "import matplotlib.pyplot as plt, seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Session- 2, Data Cleaning "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 2, Data Types "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are multiple types of data types available in the data set. some of them are numerical type and some of categorical type. You are required to get the idea about the data types after reading the data frame. \n",
    "\n",
    "Following are the some of the types of variables:\n",
    "- **Numeric data type**: banking dataset: salary, balance, duration and age.\n",
    "- **Categorical data type**: banking dataset: education, job, marital, poutcome and month etc.\n",
    "- **Ordinal data type**: banking dataset: Age group.\n",
    "- **Time and date type** \n",
    "- **Coordinates type of data**: latitude and longitude type.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Read in the Data set. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#read the data set of \"bank telemarketing campaign\" in inp0.\n",
    "inp0= pd.read_csv(\"bank_marketing_updated_v1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=dd5aefe7-84ad-40c1-90f1-8fff0f1b3e95 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('dd5aefe7-84ad-40c1-90f1-8fff0f1b3e95').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>banking marketing</th>\n",
       "      <th>Unnamed: 1</th>\n",
       "      <th>Unnamed: 2</th>\n",
       "      <th>Unnamed: 3</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "      <th>Unnamed: 5</th>\n",
       "      <th>Unnamed: 6</th>\n",
       "      <th>Unnamed: 7</th>\n",
       "      <th>Unnamed: 8</th>\n",
       "      <th>Unnamed: 9</th>\n",
       "      <th>Unnamed: 10</th>\n",
       "      <th>Unnamed: 11</th>\n",
       "      <th>Unnamed: 12</th>\n",
       "      <th>Unnamed: 13</th>\n",
       "      <th>Unnamed: 14</th>\n",
       "      <th>Unnamed: 15</th>\n",
       "      <th>Unnamed: 16</th>\n",
       "      <th>Unnamed: 17</th>\n",
       "      <th>Unnamed: 18</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>customer id and age.</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Customer salary and balance.</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Customer marital status and job with education level.</td>\n",
       "      <td>NaN</td>\n",
       "      <td>particular customer before targeted or not</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Loan types: loans or housing loans</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Contact type</td>\n",
       "      <td>NaN</td>\n",
       "      <td>month of contact</td>\n",
       "      <td>duration of call</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>outcome of previous contact</td>\n",
       "      <td>response of customer after call happned</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>customerid</td>\n",
       "      <td>age</td>\n",
       "      <td>salary</td>\n",
       "      <td>balance</td>\n",
       "      <td>marital</td>\n",
       "      <td>jobedu</td>\n",
       "      <td>targeted</td>\n",
       "      <td>default</td>\n",
       "      <td>housing</td>\n",
       "      <td>loan</td>\n",
       "      <td>contact</td>\n",
       "      <td>day</td>\n",
       "      <td>month</td>\n",
       "      <td>duration</td>\n",
       "      <td>campaign</td>\n",
       "      <td>pdays</td>\n",
       "      <td>previous</td>\n",
       "      <td>poutcome</td>\n",
       "      <td>response</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>58</td>\n",
       "      <td>100000</td>\n",
       "      <td>2143</td>\n",
       "      <td>married</td>\n",
       "      <td>management,tertiary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>261 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>44</td>\n",
       "      <td>60000</td>\n",
       "      <td>29</td>\n",
       "      <td>single</td>\n",
       "      <td>technician,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>151 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3</td>\n",
       "      <td>33</td>\n",
       "      <td>120000</td>\n",
       "      <td>2</td>\n",
       "      <td>married</td>\n",
       "      <td>entrepreneur,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>76 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "      banking marketing Unnamed: 1                    Unnamed: 2 Unnamed: 3  \\\n",
       "0  customer id and age.        NaN  Customer salary and balance.        NaN   \n",
       "1            customerid        age                        salary    balance   \n",
       "2                     1         58                        100000       2143   \n",
       "3                     2         44                         60000         29   \n",
       "4                     3         33                        120000          2   \n",
       "\n",
       "                                          Unnamed: 4              Unnamed: 5  \\\n",
       "0  Customer marital status and job with education...                     NaN   \n",
       "1                                            marital                  jobedu   \n",
       "2                                            married     management,tertiary   \n",
       "3                                             single    technician,secondary   \n",
       "4                                            married  entrepreneur,secondary   \n",
       "\n",
       "                                   Unnamed: 6 Unnamed: 7  \\\n",
       "0  particular customer before targeted or not        NaN   \n",
       "1                                    targeted    default   \n",
       "2                                         yes         no   \n",
       "3                                         yes         no   \n",
       "4                                         yes         no   \n",
       "\n",
       "                           Unnamed: 8 Unnamed: 9   Unnamed: 10 Unnamed: 11  \\\n",
       "0  Loan types: loans or housing loans        NaN  Contact type         NaN   \n",
       "1                             housing       loan       contact         day   \n",
       "2                                 yes         no       unknown           5   \n",
       "3                                 yes         no       unknown           5   \n",
       "4                                 yes        yes       unknown           5   \n",
       "\n",
       "        Unnamed: 12       Unnamed: 13 Unnamed: 14 Unnamed: 15 Unnamed: 16  \\\n",
       "0  month of contact  duration of call         NaN         NaN         NaN   \n",
       "1             month          duration    campaign       pdays    previous   \n",
       "2         may, 2017           261 sec           1          -1           0   \n",
       "3         may, 2017           151 sec           1          -1           0   \n",
       "4         may, 2017            76 sec           1          -1           0   \n",
       "\n",
       "                   Unnamed: 17                              Unnamed: 18  \n",
       "0  outcome of previous contact  response of customer after call happned  \n",
       "1                     poutcome                                 response  \n",
       "2                      unknown                                       no  \n",
       "3                      unknown                                       no  \n",
       "4                      unknown                                       no  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Print the head of the data frame.\n",
    "inp0.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 3, Fixing the Rows and Columns "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Checklist for fixing rows:\n",
    "- **Delete summary rows**: Total and Subtotal rows\n",
    "- **Delete incorrect rows**: Header row and footer row\n",
    "- **Delete extra rows**: Column number, indicators, Blank rows, Page No.\n",
    "\n",
    "Checklist for fixing columns:\n",
    "- **Merge columns for creating unique identifiers**, if needed, for example, merge the columns State and City into the column Full address.\n",
    "- **Split columns to get more data**: Split the Address column to get State and City columns to analyse each separately. \n",
    "- **Add column names**: Add column names if missing.\n",
    "- **Rename columns consistently**: Abbreviations, encoded columns.\n",
    "- **Delete columns**: Delete unnecessary columns.\n",
    "- **Align misaligned columns**: The data set may have shifted columns, which you need to align correctly.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Read the file without unnecessary headers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#read the file in inp0 without first two rows as it is of no use.\n",
    "inp0=pd.read_csv(\"bank_marketing_updated_v1.csv\", skiprows= 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=4e830dc4-e781-40a8-9239-e9788eac9d84 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('4e830dc4-e781-40a8-9239-e9788eac9d84').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>customerid</th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>balance</th>\n",
       "      <th>marital</th>\n",
       "      <th>jobedu</th>\n",
       "      <th>targeted</th>\n",
       "      <th>default</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>response</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>58.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>2143</td>\n",
       "      <td>married</td>\n",
       "      <td>management,tertiary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>261 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>44.0</td>\n",
       "      <td>60000</td>\n",
       "      <td>29</td>\n",
       "      <td>single</td>\n",
       "      <td>technician,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>151 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "      <td>120000</td>\n",
       "      <td>2</td>\n",
       "      <td>married</td>\n",
       "      <td>entrepreneur,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>76 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>47.0</td>\n",
       "      <td>20000</td>\n",
       "      <td>1506</td>\n",
       "      <td>married</td>\n",
       "      <td>blue-collar,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>92 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>33.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>single</td>\n",
       "      <td>unknown,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>198 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "   customerid   age  salary  balance  marital                  jobedu  \\\n",
       "0           1  58.0  100000     2143  married     management,tertiary   \n",
       "1           2  44.0   60000       29   single    technician,secondary   \n",
       "2           3  33.0  120000        2  married  entrepreneur,secondary   \n",
       "3           4  47.0   20000     1506  married     blue-collar,unknown   \n",
       "4           5  33.0       0        1   single         unknown,unknown   \n",
       "\n",
       "  targeted default housing loan  contact  day      month duration  campaign  \\\n",
       "0      yes      no     yes   no  unknown    5  may, 2017  261 sec         1   \n",
       "1      yes      no     yes   no  unknown    5  may, 2017  151 sec         1   \n",
       "2      yes      no     yes  yes  unknown    5  may, 2017   76 sec         1   \n",
       "3       no      no     yes   no  unknown    5  may, 2017   92 sec         1   \n",
       "4       no      no      no   no  unknown    5  may, 2017  198 sec         1   \n",
       "\n",
       "   pdays  previous poutcome response  \n",
       "0     -1         0  unknown       no  \n",
       "1     -1         0  unknown       no  \n",
       "2     -1         0  unknown       no  \n",
       "3     -1         0  unknown       no  \n",
       "4     -1         0  unknown       no  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print the head of the data frame.\n",
    "inp0.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dropping customer id column. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=4b0d2da9-679a-4565-9166-719e1711d79b style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('4b0d2da9-679a-4565-9166-719e1711d79b').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>balance</th>\n",
       "      <th>marital</th>\n",
       "      <th>jobedu</th>\n",
       "      <th>targeted</th>\n",
       "      <th>default</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>response</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>58.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>2143</td>\n",
       "      <td>married</td>\n",
       "      <td>management,tertiary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>261 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.0</td>\n",
       "      <td>60000</td>\n",
       "      <td>29</td>\n",
       "      <td>single</td>\n",
       "      <td>technician,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>151 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>33.0</td>\n",
       "      <td>120000</td>\n",
       "      <td>2</td>\n",
       "      <td>married</td>\n",
       "      <td>entrepreneur,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>76 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47.0</td>\n",
       "      <td>20000</td>\n",
       "      <td>1506</td>\n",
       "      <td>married</td>\n",
       "      <td>blue-collar,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>92 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>single</td>\n",
       "      <td>unknown,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>198 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "    age  salary  balance  marital                  jobedu targeted default  \\\n",
       "0  58.0  100000     2143  married     management,tertiary      yes      no   \n",
       "1  44.0   60000       29   single    technician,secondary      yes      no   \n",
       "2  33.0  120000        2  married  entrepreneur,secondary      yes      no   \n",
       "3  47.0   20000     1506  married     blue-collar,unknown       no      no   \n",
       "4  33.0       0        1   single         unknown,unknown       no      no   \n",
       "\n",
       "  housing loan  contact  day      month duration  campaign  pdays  previous  \\\n",
       "0     yes   no  unknown    5  may, 2017  261 sec         1     -1         0   \n",
       "1     yes   no  unknown    5  may, 2017  151 sec         1     -1         0   \n",
       "2     yes  yes  unknown    5  may, 2017   76 sec         1     -1         0   \n",
       "3     yes   no  unknown    5  may, 2017   92 sec         1     -1         0   \n",
       "4      no   no  unknown    5  may, 2017  198 sec         1     -1         0   \n",
       "\n",
       "  poutcome response  \n",
       "0  unknown       no  \n",
       "1  unknown       no  \n",
       "2  unknown       no  \n",
       "3  unknown       no  \n",
       "4  unknown       no  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#drop the customer id as it is of no use.\n",
    "inp0.drop(\"customerid\", axis=1, inplace=True)\n",
    "inp0.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dividing \"jobedu\" column into job and education categories. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=9a635f56-8ad1-4dd6-a8e7-5a9b8bc7e249 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('9a635f56-8ad1-4dd6-a8e7-5a9b8bc7e249').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>balance</th>\n",
       "      <th>marital</th>\n",
       "      <th>jobedu</th>\n",
       "      <th>targeted</th>\n",
       "      <th>default</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>response</th>\n",
       "      <th>job</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>58.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>2143</td>\n",
       "      <td>married</td>\n",
       "      <td>management,tertiary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>261 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>management</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.0</td>\n",
       "      <td>60000</td>\n",
       "      <td>29</td>\n",
       "      <td>single</td>\n",
       "      <td>technician,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>151 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>technician</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>33.0</td>\n",
       "      <td>120000</td>\n",
       "      <td>2</td>\n",
       "      <td>married</td>\n",
       "      <td>entrepreneur,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>76 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>entrepreneur</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47.0</td>\n",
       "      <td>20000</td>\n",
       "      <td>1506</td>\n",
       "      <td>married</td>\n",
       "      <td>blue-collar,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>92 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>blue-collar</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>single</td>\n",
       "      <td>unknown,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>198 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "    age  salary  balance  marital                  jobedu targeted default  \\\n",
       "0  58.0  100000     2143  married     management,tertiary      yes      no   \n",
       "1  44.0   60000       29   single    technician,secondary      yes      no   \n",
       "2  33.0  120000        2  married  entrepreneur,secondary      yes      no   \n",
       "3  47.0   20000     1506  married     blue-collar,unknown       no      no   \n",
       "4  33.0       0        1   single         unknown,unknown       no      no   \n",
       "\n",
       "  housing loan  contact  day      month duration  campaign  pdays  previous  \\\n",
       "0     yes   no  unknown    5  may, 2017  261 sec         1     -1         0   \n",
       "1     yes   no  unknown    5  may, 2017  151 sec         1     -1         0   \n",
       "2     yes  yes  unknown    5  may, 2017   76 sec         1     -1         0   \n",
       "3     yes   no  unknown    5  may, 2017   92 sec         1     -1         0   \n",
       "4      no   no  unknown    5  may, 2017  198 sec         1     -1         0   \n",
       "\n",
       "  poutcome response           job  \n",
       "0  unknown       no    management  \n",
       "1  unknown       no    technician  \n",
       "2  unknown       no  entrepreneur  \n",
       "3  unknown       no   blue-collar  \n",
       "4  unknown       no       unknown  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Extract job in newly created 'job' column from \"jobedu\" column.\n",
    "inp0['job']=inp0.jobedu.apply(lambda x: x.split(\",\")[0])\n",
    "inp0.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=c79a5bfc-601c-46ba-8574-3e77555f8114 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('c79a5bfc-601c-46ba-8574-3e77555f8114').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>balance</th>\n",
       "      <th>marital</th>\n",
       "      <th>jobedu</th>\n",
       "      <th>targeted</th>\n",
       "      <th>default</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>response</th>\n",
       "      <th>job</th>\n",
       "      <th>education</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>58.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>2143</td>\n",
       "      <td>married</td>\n",
       "      <td>management,tertiary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>261 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>management</td>\n",
       "      <td>tertiary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.0</td>\n",
       "      <td>60000</td>\n",
       "      <td>29</td>\n",
       "      <td>single</td>\n",
       "      <td>technician,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>151 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>technician</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>33.0</td>\n",
       "      <td>120000</td>\n",
       "      <td>2</td>\n",
       "      <td>married</td>\n",
       "      <td>entrepreneur,secondary</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>76 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>entrepreneur</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47.0</td>\n",
       "      <td>20000</td>\n",
       "      <td>1506</td>\n",
       "      <td>married</td>\n",
       "      <td>blue-collar,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>92 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>blue-collar</td>\n",
       "      <td>unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>single</td>\n",
       "      <td>unknown,unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>198 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>unknown</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "    age  salary  balance  marital                  jobedu targeted default  \\\n",
       "0  58.0  100000     2143  married     management,tertiary      yes      no   \n",
       "1  44.0   60000       29   single    technician,secondary      yes      no   \n",
       "2  33.0  120000        2  married  entrepreneur,secondary      yes      no   \n",
       "3  47.0   20000     1506  married     blue-collar,unknown       no      no   \n",
       "4  33.0       0        1   single         unknown,unknown       no      no   \n",
       "\n",
       "  housing loan  contact  day      month duration  campaign  pdays  previous  \\\n",
       "0     yes   no  unknown    5  may, 2017  261 sec         1     -1         0   \n",
       "1     yes   no  unknown    5  may, 2017  151 sec         1     -1         0   \n",
       "2     yes  yes  unknown    5  may, 2017   76 sec         1     -1         0   \n",
       "3     yes   no  unknown    5  may, 2017   92 sec         1     -1         0   \n",
       "4      no   no  unknown    5  may, 2017  198 sec         1     -1         0   \n",
       "\n",
       "  poutcome response           job  education  \n",
       "0  unknown       no    management   tertiary  \n",
       "1  unknown       no    technician  secondary  \n",
       "2  unknown       no  entrepreneur  secondary  \n",
       "3  unknown       no   blue-collar    unknown  \n",
       "4  unknown       no       unknown    unknown  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Extract education in newly created 'education' column from \"jobedu\" column.\n",
    "inp0['education']=inp0.jobedu.apply(lambda x: x.split(\",\")[1])\n",
    "inp0.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=369cb49c-2ce7-41aa-a6af-f84fd9826a4e style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('369cb49c-2ce7-41aa-a6af-f84fd9826a4e').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>balance</th>\n",
       "      <th>marital</th>\n",
       "      <th>targeted</th>\n",
       "      <th>default</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>response</th>\n",
       "      <th>job</th>\n",
       "      <th>education</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>58.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>2143</td>\n",
       "      <td>married</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>261 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>management</td>\n",
       "      <td>tertiary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>44.0</td>\n",
       "      <td>60000</td>\n",
       "      <td>29</td>\n",
       "      <td>single</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>151 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>technician</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>33.0</td>\n",
       "      <td>120000</td>\n",
       "      <td>2</td>\n",
       "      <td>married</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>76 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>entrepreneur</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>47.0</td>\n",
       "      <td>20000</td>\n",
       "      <td>1506</td>\n",
       "      <td>married</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>92 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>blue-collar</td>\n",
       "      <td>unknown</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>33.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>single</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may, 2017</td>\n",
       "      <td>198 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>unknown</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "    age  salary  balance  marital targeted default housing loan  contact  day  \\\n",
       "0  58.0  100000     2143  married      yes      no     yes   no  unknown    5   \n",
       "1  44.0   60000       29   single      yes      no     yes   no  unknown    5   \n",
       "2  33.0  120000        2  married      yes      no     yes  yes  unknown    5   \n",
       "3  47.0   20000     1506  married       no      no     yes   no  unknown    5   \n",
       "4  33.0       0        1   single       no      no      no   no  unknown    5   \n",
       "\n",
       "       month duration  campaign  pdays  previous poutcome response  \\\n",
       "0  may, 2017  261 sec         1     -1         0  unknown       no   \n",
       "1  may, 2017  151 sec         1     -1         0  unknown       no   \n",
       "2  may, 2017   76 sec         1     -1         0  unknown       no   \n",
       "3  may, 2017   92 sec         1     -1         0  unknown       no   \n",
       "4  may, 2017  198 sec         1     -1         0  unknown       no   \n",
       "\n",
       "            job  education  \n",
       "0    management   tertiary  \n",
       "1    technician  secondary  \n",
       "2  entrepreneur  secondary  \n",
       "3   blue-collar    unknown  \n",
       "4       unknown    unknown  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#drop the \"jobedu\" column from the dataframe.\n",
    "inp0.drop('jobedu',axis= 1, inplace= True)\n",
    "inp0.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Extract the month from column 'month' "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=0a1ce8c1-60f2-4911-a3ce-e73d146ef0f8 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('0a1ce8c1-60f2-4911-a3ce-e73d146ef0f8').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>balance</th>\n",
       "      <th>marital</th>\n",
       "      <th>targeted</th>\n",
       "      <th>default</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>response</th>\n",
       "      <th>job</th>\n",
       "      <th>education</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>189</th>\n",
       "      <td>31.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>0</td>\n",
       "      <td>single</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>562 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>management</td>\n",
       "      <td>tertiary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>769</th>\n",
       "      <td>39.0</td>\n",
       "      <td>20000</td>\n",
       "      <td>245</td>\n",
       "      <td>married</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>7</td>\n",
       "      <td>NaN</td>\n",
       "      <td>148 sec</td>\n",
       "      <td>3</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>blue-collar</td>\n",
       "      <td>primary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>860</th>\n",
       "      <td>33.0</td>\n",
       "      <td>55000</td>\n",
       "      <td>165</td>\n",
       "      <td>married</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>7</td>\n",
       "      <td>NaN</td>\n",
       "      <td>111 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>retired</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1267</th>\n",
       "      <td>36.0</td>\n",
       "      <td>50000</td>\n",
       "      <td>114</td>\n",
       "      <td>married</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>8</td>\n",
       "      <td>NaN</td>\n",
       "      <td>147 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>admin.</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1685</th>\n",
       "      <td>34.0</td>\n",
       "      <td>20000</td>\n",
       "      <td>457</td>\n",
       "      <td>married</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>266 sec</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "      <td>blue-collar</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43001</th>\n",
       "      <td>35.0</td>\n",
       "      <td>60000</td>\n",
       "      <td>353</td>\n",
       "      <td>single</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>11</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.86666666666667 min</td>\n",
       "      <td>1</td>\n",
       "      <td>183</td>\n",
       "      <td>1</td>\n",
       "      <td>success</td>\n",
       "      <td>yes</td>\n",
       "      <td>self-employed</td>\n",
       "      <td>tertiary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43021</th>\n",
       "      <td>52.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>4675</td>\n",
       "      <td>married</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.01666666666667 min</td>\n",
       "      <td>3</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>yes</td>\n",
       "      <td>management</td>\n",
       "      <td>tertiary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43323</th>\n",
       "      <td>54.0</td>\n",
       "      <td>70000</td>\n",
       "      <td>0</td>\n",
       "      <td>divorced</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>18</td>\n",
       "      <td>NaN</td>\n",
       "      <td>6.03333333333333 min</td>\n",
       "      <td>1</td>\n",
       "      <td>290</td>\n",
       "      <td>3</td>\n",
       "      <td>success</td>\n",
       "      <td>yes</td>\n",
       "      <td>services</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44131</th>\n",
       "      <td>27.0</td>\n",
       "      <td>100000</td>\n",
       "      <td>843</td>\n",
       "      <td>single</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.05 min</td>\n",
       "      <td>2</td>\n",
       "      <td>185</td>\n",
       "      <td>1</td>\n",
       "      <td>success</td>\n",
       "      <td>no</td>\n",
       "      <td>management</td>\n",
       "      <td>secondary</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44732</th>\n",
       "      <td>23.0</td>\n",
       "      <td>4000</td>\n",
       "      <td>508</td>\n",
       "      <td>single</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>8</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.5 min</td>\n",
       "      <td>1</td>\n",
       "      <td>92</td>\n",
       "      <td>1</td>\n",
       "      <td>failure</td>\n",
       "      <td>no</td>\n",
       "      <td>student</td>\n",
       "      <td>tertiary</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "        age  salary  balance   marital targeted default housing loan  \\\n",
       "189    31.0  100000        0    single       no      no     yes   no   \n",
       "769    39.0   20000      245   married      yes      no     yes   no   \n",
       "860    33.0   55000      165   married      yes      no      no   no   \n",
       "1267   36.0   50000      114   married      yes      no     yes  yes   \n",
       "1685   34.0   20000      457   married      yes      no     yes   no   \n",
       "1899   49.0   16000      164  divorced      yes      no     yes   no   \n",
       "2433   26.0   60000     3825   married      yes      no     yes   no   \n",
       "2612   38.0   50000      446    single       no      no     yes   no   \n",
       "2747   48.0  120000     2550   married       no      no     yes   no   \n",
       "3556   41.0   20000       59   married      yes      no     yes   no   \n",
       "3890   56.0   55000     4391   married       no      no     yes   no   \n",
       "5311   22.0   20000        0    single      yes      no     yes   no   \n",
       "6265   32.0   50000       13    single      yes      no     yes   no   \n",
       "6396   24.0   70000        0   married      yes      no     yes   no   \n",
       "8433   38.0   60000    12926    single      yes      no     yes   no   \n",
       "8792   24.0   50000      262   married      yes      no     yes   no   \n",
       "10627  45.0   60000      533   married      yes      no     yes   no   \n",
       "11016  46.0   70000      741   married      yes      no      no   no   \n",
       "11284  44.0   16000     1059    single      yes      no      no   no   \n",
       "11394  54.0   60000      415   married      yes      no     yes   no   \n",
       "14502  35.0   70000      819   married      yes      no     yes   no   \n",
       "15795  38.0   20000      -41   married      yes      no     yes   no   \n",
       "16023  35.0   60000      328   married      yes      no     yes   no   \n",
       "16850  45.0   55000       25   married      yes      no      no  yes   \n",
       "17568  56.0   70000        0   married       no      no      no   no   \n",
       "18431  42.0   70000      247    single      yes      no     yes   no   \n",
       "18942  49.0   50000      949   married      yes      no      no   no   \n",
       "19118  38.0   50000     1980   married      yes      no      no   no   \n",
       "19769  36.0  100000      162   married      yes      no     yes   no   \n",
       "21777  56.0   16000      605   married      yes      no      no   no   \n",
       "21962  36.0   60000     1044    single      yes      no     yes   no   \n",
       "23897  46.0   20000      123   married      yes      no      no   no   \n",
       "25658  35.0   60000     8647   married      yes      no      no   no   \n",
       "27480  31.0  100000     3283    single       no      no      no   no   \n",
       "28693  26.0   16000      543   married      yes      no      no   no   \n",
       "30740  32.0  100000     2770    single       no      no      no   no   \n",
       "31551  54.0   55000      136   married      yes      no     yes   no   \n",
       "35773  52.0   20000       33   married       no      no      no   no   \n",
       "37194  36.0   20000     1969   married      yes      no     yes  yes   \n",
       "37819  34.0   20000      237   married      yes      no     yes   no   \n",
       "38158  34.0   60000     1317  divorced       no      no     yes   no   \n",
       "39188  30.0   60000      778    single      yes      no     yes   no   \n",
       "41090  35.0  100000     7218    single       no      no      no   no   \n",
       "41434  43.0  100000    13450   married      yes      no     yes   no   \n",
       "41606  25.0  100000      808    single       no      no      no   no   \n",
       "43001  35.0   60000      353    single       no      no      no   no   \n",
       "43021  52.0  100000     4675   married      yes      no      no   no   \n",
       "43323  54.0   70000        0  divorced      yes      no      no   no   \n",
       "44131  27.0  100000      843    single      yes      no      no   no   \n",
       "44732  23.0    4000      508    single       no      no      no   no   \n",
       "\n",
       "         contact  day month               duration  campaign  pdays  previous  \\\n",
       "189      unknown    5   NaN                562 sec         1     -1         0   \n",
       "769      unknown    7   NaN                148 sec         3     -1         0   \n",
       "860      unknown    7   NaN                111 sec         1     -1         0   \n",
       "1267     unknown    8   NaN                147 sec         1     -1         0   \n",
       "1685     unknown    9   NaN                266 sec         1     -1         0   \n",
       "1899     unknown    9   NaN               1080 sec         5     -1         0   \n",
       "2433     unknown   13   NaN                107 sec         1     -1         0   \n",
       "2612     unknown   13   NaN                386 sec         1     -1         0   \n",
       "2747     unknown   14   NaN                175 sec         3     -1         0   \n",
       "3556     unknown   15   NaN                 75 sec         8     -1         0   \n",
       "3890     unknown   16   NaN                291 sec         1     -1         0   \n",
       "5311     unknown   23   NaN                816 sec         2     -1         0   \n",
       "6265     unknown   27   NaN                 88 sec         2     -1         0   \n",
       "6396     unknown   27   NaN                299 sec         1     -1         0   \n",
       "8433     unknown    3   NaN                280 sec         1     -1         0   \n",
       "8792     unknown    4   NaN                 69 sec         3     -1         0   \n",
       "10627    unknown   16   NaN                332 sec         2     -1         0   \n",
       "11016    unknown   17   NaN                161 sec         3     -1         0   \n",
       "11284    unknown   18   NaN               2093 sec         1     -1         0   \n",
       "11394    unknown   19   NaN                 34 sec        31     -1         0   \n",
       "14502  telephone   14   NaN                1.7 min        14     -1         0   \n",
       "15795   cellular   21   NaN   1.13333333333333 min        10     -1         0   \n",
       "16023   cellular   22   NaN               10.9 min         2     -1         0   \n",
       "16850   cellular   25   NaN   1.91666666666667 min         3     -1         0   \n",
       "17568   cellular   29   NaN   1.38333333333333 min         2     -1         0   \n",
       "18431   cellular   31   NaN                1.9 min         2     -1         0   \n",
       "18942   cellular    4   NaN   1.51666666666667 min         1     -1         0   \n",
       "19118   cellular    5   NaN   2.93333333333333 min         2     -1         0   \n",
       "19769   cellular    8   NaN               1.25 min         2     -1         0   \n",
       "21777   cellular   19   NaN               3.45 min         6     -1         0   \n",
       "21962   cellular   20   NaN               0.25 min        19     -1         0   \n",
       "23897   cellular   29   NaN                2.8 min         2     -1         0   \n",
       "25658   cellular   19   NaN   2.33333333333333 min         2     -1         0   \n",
       "27480   cellular   21   NaN   6.28333333333333 min         1     -1         0   \n",
       "28693   cellular   30   NaN   2.81666666666667 min         3     -1         0   \n",
       "30740  telephone    6   NaN  0.733333333333333 min         9     -1         0   \n",
       "31551   cellular    3   NaN   5.86666666666667 min         1    332         2   \n",
       "35773  telephone    8   NaN   5.01666666666667 min         1     -1         0   \n",
       "37194   cellular   13   NaN               1.45 min         1     -1         0   \n",
       "37819   cellular   14   NaN   1.91666666666667 min         3     -1         0   \n",
       "38158   cellular   15   NaN   3.98333333333333 min         1     -1         0   \n",
       "39188   cellular   18   NaN  0.366666666666667 min         2    346         2   \n",
       "41090   cellular   14   NaN   3.73333333333333 min         3     -1         0   \n",
       "41434   cellular    4   NaN   2.13333333333333 min         1     -1         0   \n",
       "41606   cellular   18   NaN               4.45 min         2    114         2   \n",
       "43001   cellular   11   NaN   5.86666666666667 min         1    183         1   \n",
       "43021   cellular   12   NaN   3.01666666666667 min         3     -1         0   \n",
       "43323   cellular   18   NaN   6.03333333333333 min         1    290         3   \n",
       "44131   cellular   12   NaN               2.05 min         2    185         1   \n",
       "44732   cellular    8   NaN                3.5 min         1     92         1   \n",
       "\n",
       "      poutcome response            job  education  \n",
       "189    unknown       no     management   tertiary  \n",
       "769    unknown       no    blue-collar    primary  \n",
       "860    unknown       no        retired  secondary  \n",
       "1267   unknown       no         admin.  secondary  \n",
       "1685   unknown       no    blue-collar  secondary  \n",
       "1899   unknown       no      housemaid    primary  \n",
       "2433   unknown       no     technician   tertiary  \n",
       "2612   unknown       no         admin.    unknown  \n",
       "2747   unknown       no   entrepreneur    unknown  \n",
       "3556   unknown       no    blue-collar  secondary  \n",
       "3890   unknown       no        retired    unknown  \n",
       "5311   unknown       no    blue-collar  secondary  \n",
       "6265   unknown       no         admin.  secondary  \n",
       "6396   unknown       no       services   tertiary  \n",
       "8433   unknown       no     technician  secondary  \n",
       "8792   unknown       no         admin.  secondary  \n",
       "10627  unknown       no     technician   tertiary  \n",
       "11016  unknown       no       services    primary  \n",
       "11284  unknown      yes      housemaid    primary  \n",
       "11394  unknown       no     technician  secondary  \n",
       "14502  unknown       no       services  secondary  \n",
       "15795  unknown       no    blue-collar    primary  \n",
       "16023  unknown      yes     technician   tertiary  \n",
       "16850  unknown       no        retired    primary  \n",
       "17568  unknown       no       services    unknown  \n",
       "18431  unknown       no       services  secondary  \n",
       "18942  unknown       no         admin.  secondary  \n",
       "19118  unknown       no         admin.   tertiary  \n",
       "19769  unknown       no     management   tertiary  \n",
       "21777  unknown       no      housemaid    primary  \n",
       "21962  unknown       no     technician  secondary  \n",
       "23897  unknown       no    blue-collar    primary  \n",
       "25658  unknown       no  self-employed   tertiary  \n",
       "27480  unknown       no     management   tertiary  \n",
       "28693  unknown       no      housemaid   tertiary  \n",
       "30740  unknown       no     management   tertiary  \n",
       "31551  failure       no        retired    primary  \n",
       "35773  unknown       no    blue-collar    unknown  \n",
       "37194  unknown       no    blue-collar  secondary  \n",
       "37819  unknown       no    blue-collar  secondary  \n",
       "38158  unknown       no     technician   tertiary  \n",
       "39188  failure       no     technician  secondary  \n",
       "41090  unknown       no     management   tertiary  \n",
       "41434  unknown       no     management   tertiary  \n",
       "41606  failure      yes     management   tertiary  \n",
       "43001  success      yes  self-employed   tertiary  \n",
       "43021  unknown      yes     management   tertiary  \n",
       "43323  success      yes       services  secondary  \n",
       "44131  success       no     management  secondary  \n",
       "44732  failure       no        student   tertiary  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp0[inp0.month.apply(lambda x: isinstance(x,float))== True]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "let's check the missing values in month column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age          20\n",
       "salary        0\n",
       "balance       0\n",
       "marital       0\n",
       "targeted      0\n",
       "default       0\n",
       "housing       0\n",
       "loan          0\n",
       "contact       0\n",
       "day           0\n",
       "month        50\n",
       "duration      0\n",
       "campaign      0\n",
       "pdays         0\n",
       "previous      0\n",
       "poutcome      0\n",
       "response     30\n",
       "job           0\n",
       "education     0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp0.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 4, Impute/Remove missing values "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Take aways from the lecture on missing values:\n",
    "\n",
    "- **Set values as missing values**: Identify values that indicate missing data, for example, treat blank strings, \"NA\", \"XX\", \"999\", etc., as missing.\n",
    "- **Adding is good, exaggerating is bad**: You should try to get information from reliable external sources as much as possible, but if you can’t, then it is better to retain missing values rather than exaggerating the existing rows/columns.\n",
    "- **Delete rows and columns**: Rows can be deleted if the number of missing values is insignificant, as this would not impact the overall analysis results. Columns can be removed if the missing values are quite significant in number.\n",
    "- **Fill partial missing values using business judgement**: Such values include missing time zone, century, etc. These values can be identified easily.\n",
    "\n",
    "Types of missing values:\n",
    "- **MCAR**: It stands for Missing completely at random (the reason behind the missing value is not dependent on any other feature).\n",
    "- **MAR**: It stands for Missing at random (the reason behind the missing value may be associated with some other features).\n",
    "- **MNAR**: It stands for Missing not at random (there is a specific reason behind the missing value).\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### handling missing values in age column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#count the missing values in age column.\n",
    "inp0.age.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(45211, 19)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#pring the shape of dataframe inp0\n",
    "inp0.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.04423702196368141"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the percentage of missing values in age column.\n",
    "float(100.0*20/45211)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Drop the records with age missing. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(45191, 19)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#drop the records with age missing in inp0 and copy in inp1 dataframe.\n",
    "inp1=inp0[-inp0.age.isnull()].copy()\n",
    "inp1.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### handling missing values in month column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#count the missing values in month column in inp1.\n",
    "inp1.month.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.11064149941360005"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print the percentage of each month in the data frame inp1.\n",
    "float(100.0*50/45191)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "may, 2017    0.304380\n",
       "jul, 2017    0.152522\n",
       "aug, 2017    0.138123\n",
       "jun, 2017    0.118141\n",
       "nov, 2017    0.087880\n",
       "apr, 2017    0.064908\n",
       "feb, 2017    0.058616\n",
       "jan, 2017    0.031058\n",
       "oct, 2017    0.016327\n",
       "sep, 2017    0.012760\n",
       "mar, 2017    0.010545\n",
       "dec, 2017    0.004741\n",
       "Name: month, dtype: float64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1.month.value_counts(normalize = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'may, 2017'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#find the mode of month in inp1\n",
    "month_mode=inp1.month.mode()[0]\n",
    "month_mode"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "may, 2017    0.305149\n",
       "jul, 2017    0.152353\n",
       "aug, 2017    0.137970\n",
       "jun, 2017    0.118010\n",
       "nov, 2017    0.087783\n",
       "apr, 2017    0.064836\n",
       "feb, 2017    0.058551\n",
       "jan, 2017    0.031024\n",
       "oct, 2017    0.016309\n",
       "sep, 2017    0.012746\n",
       "mar, 2017    0.010533\n",
       "dec, 2017    0.004735\n",
       "Name: month, dtype: float64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# fill the missing values with mode value of month in inp1.\n",
    "inp1.month.fillna(month_mode, inplace= True)\n",
    "inp1.month.value_counts(normalize= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#let's see the null values in the month column.\n",
    "inp1.month.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### handling missing values in response column "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#count the missing values in response column in inp1.\n",
    "inp1.response.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.06638489964816004"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the percentage of missing values in response column. \n",
    "float(100.0*30/45191)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Target variable is better of not imputed.\n",
    "- Drop the records with missing values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#drop the records with response missings in inp1.\n",
    "inp1= inp1[~inp1.response.isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age          0\n",
       "salary       0\n",
       "balance      0\n",
       "marital      0\n",
       "targeted     0\n",
       "default      0\n",
       "housing      0\n",
       "loan         0\n",
       "contact      0\n",
       "day          0\n",
       "month        0\n",
       "duration     0\n",
       "campaign     0\n",
       "pdays        0\n",
       "previous     0\n",
       "poutcome     0\n",
       "response     0\n",
       "job          0\n",
       "education    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the missing values in each column of data frame: inp1.\n",
    "inp1.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### handling pdays column. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    45161.000000\n",
       "mean        40.182015\n",
       "std        100.079372\n",
       "min         -1.000000\n",
       "25%         -1.000000\n",
       "50%         -1.000000\n",
       "75%         -1.000000\n",
       "max        871.000000\n",
       "Name: pdays, dtype: float64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the pdays column of inp1.\n",
    "inp1.pdays.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-1 indicates the missing values.\n",
    "Missing value does not always be present as null.\n",
    "How to handle it:\n",
    "\n",
    "Objective is:\n",
    "- you should ignore the missing values in the calculations\n",
    "- simply make it missing - replace -1 with NaN.\n",
    "- all summary statistics- mean, median etc. we will ignore the missing values of pdays."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    8246.000000\n",
       "mean      224.542202\n",
       "std       115.210792\n",
       "min         1.000000\n",
       "25%       133.000000\n",
       "50%       195.000000\n",
       "75%       327.000000\n",
       "max       871.000000\n",
       "Name: pdays, dtype: float64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the pdays column with considering the -1 values.\n",
    "inp1.loc[inp1.pdays<0,\"pdays\"]=np.NaN\n",
    "inp1.pdays.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 5, Handling Outliers "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Major approaches to the treat outliers:\n",
    " \t\t\n",
    "- **Imputation**\n",
    "- **Deletion of outliers**\n",
    "- **Binning of values**\n",
    "- **Cap the outlier**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Age variable "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    45161.000000\n",
       "mean        40.935763\n",
       "std         10.618790\n",
       "min         18.000000\n",
       "25%         33.000000\n",
       "50%         39.000000\n",
       "75%         48.000000\n",
       "max         95.000000\n",
       "Name: age, dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the age variable in inp1.\n",
    "inp1.age.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the histogram of age variable.\n",
    "inp1.age.plot.hist()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAOqklEQVR4nO3dfWxd9XnA8e+TmA4nAZqUF2UJm1u5K4OyphAxOiZ254QtkAbExhAgBpGmoQmaF5g0bcBGogUkpIGCMpjE2hXYRiuVlpcgyICGTFulbbVbXkIJ42pNWzJK0oSl5IUOJ7/9cY+D7TkkJraf4/j7ka58zznX5z6xfb85Pr6+jlIKkqSxNyl7AEmaqAywJCUxwJKUxABLUhIDLElJ2oZz4xNPPLF0dHSM0iiSdHTq6en5SSnlpMHrhxXgjo4Ouru7R24qSZoAIuIHQ633FIQkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1KSYf1NOB3amjVraDabo7b/LVu2ADBr1qxRu4/h6uzsZMmSJdljSOOOAR5hzWaTFza+yr4pM0Zl/5P37ATgxz+rx6du8p4d2SNI41Y9HsVHmX1TZrD3tItGZd/tm54CGLX9D1ffPJKGz3PAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlGRMArxmzRrWrFkzFnclHRV8zEwMbWNxJ81mcyzuRjpq+JiZGDwFIUlJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHAkpTEAEtSEgMsSUkMsCQlMcCSlMQAS1ISAyxJSQywJCUxwJKUxABLUhIDLElJDLAkJTHA0jjQaDQOXEZiuauri0ajwbx584bcPn/+fBqNBhdccAEAF154IY1Gg4ULFwIwb948Go0G8+fPB+Dqq6+m0WiwePFiAC6//HIajQZXXnklAJdccgmNRoNLL70UgDvvvJNGo8Fdd90FwOOPP06j0WDt2rVDbl+/fj2NRoPnn38egGazycKFC2k2mwB0d3fT1dVFT0/PkNv7G7xt8PL27dtZunQp27dvP+S+jpQBliag/fv3A7Bv374ht/f29gLw3nvvAbB3714Adu/ePeD9+m73xhtvALB582YAtm7dCsCbb74JwM6dOwF4++23AXj66acBDgR39erVANx9991Dbr/jjjsAuP322wFYtWoVu3fvZtWqVQCsWLGC/fv3c9tttw25vb/B2wYvP/jgg7z88ss89NBDh9zXkTLAUs31HZUeLct9R819brjhBkopAJRSuP766wdsX758+YHQ9/b28vDDDx8I/ebNm3niiSfYtWsXALt27WLt2rUDtvc/cm02mwO2rV+/fsByT08P69ato5TCunXr6O7uPui+RkL0/cMPx9y5c0t3d/ew7+Syyy5j7969dHZ2Dvt9x5tms8k7/1vYPeeKUdl/+6anANh72kWjsv/hmvrCVznuIzEhPrdjqdls0t7eziOPPPL/AqaBIoL+HRu83NHRwQMPPADA4sWLDwQVoK2t7UDcAaZNm8a7775Lb28vbW1tHHvssQfiPnhfw5yxp5Qyd/D6Qx4BR8R1EdEdEd3btm0b9h1L0mgafBA5eLl/cPtfBwbEF1pH0P2PtvvHd6j3P1Jth7pBKeV+4H5oHQF/mDuZNWsWAPfcc8+HefdxZdmyZfT811vZY4yZ/cceT+cnTpkQn9uxtGzZsuwRxo3DOQLuf/1Ij4BHkueAJY2ptraBx31nnHHGgOXTTz99wPKcOXMGLF933XUDlm+88cYByzfddNOA5VtvvXXI6wA333zzgOWVK1cyaVIri5MnT2bFihUH3ddIMMBSzW3YsOGoWn7uuecGLN97771EBNA6er3vvvsGbF+9evWBaLe1tXHVVVcdOBLt6Ojg4osvZtq0aUDrCHbRokUDtvf/+URnZ+eAbV1dXQOWzz77bBYsWEBEsGDBAubOnXvQfY0EAyxNQP2P8obSF7xjjjkGgPb2dgCmTp064P36bjd79mzg/W/RTz75ZABmzpwJwAknnADA9OnTgdbz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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the boxplot of age variable.\n",
    "sns.boxplot(inp1.age)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Salary variable "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     45161.000000\n",
       "mean      57004.849317\n",
       "std       32087.698810\n",
       "min           0.000000\n",
       "25%       20000.000000\n",
       "50%       60000.000000\n",
       "75%       70000.000000\n",
       "max      120000.000000\n",
       "Name: salary, dtype: float64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the salary variable of inp1.\n",
    "inp1.salary.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the boxplot of salary variable.\n",
    "sns.boxplot(inp1.salary)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Balance variable "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count     45161.000000\n",
       "mean       1362.850690\n",
       "std        3045.939589\n",
       "min       -8019.000000\n",
       "25%          72.000000\n",
       "50%         448.000000\n",
       "75%        1428.000000\n",
       "max      102127.000000\n",
       "Name: balance, dtype: float64"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the balance variable of inp1.\n",
    "inp1.balance.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAEGCAYAAABbzE8LAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAARpklEQVR4nO3da3Bc9XnH8d9jrYJkLUmEUBljUq81SxNc8JRY7YTeBic2tYUHv+FFmMlY9DKhU8Y2l4EBW64kLi9SggcjTxPIpdhNmqZNMwVfiZ0YZtoXEGkaEwgQNmW5pxhBQw1xRpL/fbFnl7Pr1WpX9urRLt/PjEZn/3v+Z5/n7PGP3bOrg4UQBACYewu8CwCADysCGACcEMAA4IQABgAnBDAAOEnUsvK5554bUqlUnUoBgOY0Njb2Vgihu3S8pgBOpVIaHR09c1UBwIeAmb1UbpxTEADghAAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJwQwADghgAHACQEMAE4IYABwQgADgBMCGACcEMAA4IQABgAnBDAAOKnp/wk334yMjOjxxx+XJC1evFiSlE6ntXHjRs+yAKAqDR3AmUxGx94al1oS+uVvEmp5/23vkgCgao1/CqIloamFXfr1p/o0tfAc72oAoGqNH8AA0KAIYABwQgADgBMCGACcEMAA4IQABgAnBDAAOCGAAcAJAQwATghgAHBCAAOAEwIYAJwQwADghAAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJwQwADghgAHACQEMAE4IYABwQgADgBMCGACcEMAA4IQABgAnBDAAOCGAAcAJAQwATghgAHBCAAOAEwIYAJwQwADghAAGACcEMAA4IYABwAkBDABOGiaAR0ZGNDIyMudzAaBeEt4FVCuTybjMBYB6aZhXwADQbAhgAHBCAAOAEwIYAJwQwADghAAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJwQwADghgAHACQEMAE4IYABwQgADgBMCGACcEMAA4IQABgAnBDAAOCGAAcAJAQwATghgAHBCAAOAEwIYAJwQwADghAAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJ4m5eJDx8XENDw9rcHBQkgrLXV1d067b39+vrVu3KoSgkydPamJiQpI0NjamFStW1PT4R48elSRdfvnlp9dIg2hpaVEikSjab5KUSCQ0OTkpSeru7tbZZ5+tl19+WZOTk+rs7NSJEyc0MjKidDqt0dFR3XrrrVqyZImuv/56bdu2TSEE7dy5U+l0WplMRps2bdLixYt13XXXaXBwUDfffLPuueceLVq0SCdOnNDrr7+uwcFBLV++XMPDw9q0aZPuvfdemZnuvPPOwvM/Pj6ubdu26cSJE3rjjTc0MjKizs7OwnHyzjvvaPPmzdqxY4ckafPmzRoeHtbu3bunPY4qiR+PR48e1R133KHBwUGtXLmy6rmbNm3S/fffXzimBwYGZGa66aabCuPV1hWvJz4nk8kU+k6n06e1rXqYTX3zSbX7qp771EIIVa/c29sbRkdHa36Q7du3a8+ePbrqqqsUQigs33jjjdOu29HRoePHj59yfzKZ1N69eyXl/iH+5OmfaWphl379qT61P7dfK3rOK/xDzfuwBO+ZkEql9NBDD2ndunWF/Z9MJgvL+fuvvfZaZbPZovvjAZ+XSCTU19enPXv2aMmSJYU569evLzz/27dv1yOPPFJUw/LlywvHydGjR5XNZpVKpSRJ2WxWyWRS77333rTHUSXx43Hfvn2anJxUIpHQ4cOHq567ZMkSvfTSS4VjOl9/KpUqjFdbV7ye+Jz8Ps7v89PZVj3Mpr75pNp9dSb2qZmNhRB6S8frfgpifHxcBw8eVAhBBw4cKCwfPHhQ4+Pj065bLnwl6fjx4xobG6v68Qnf2mSzWT388MNF+z++nM1mdeTIkUKQxu8vDd/82L59+xRCKJpz4MABjY+PF57z0hoOHDigEIL2799fmJfNZgvLx48fn/Y4qiR+jO3du7dQ8+TkpI4cOVL13Gw2Wzim9+/fX1R7LXXFtxmfk8lkivrOZDKz3lY9zKa++aTafVXvfVr3AN61a5dOnjwpSZqYmCi8JZ6amtLu3bunXbeSW265RZs3b8496SenCuMLTrxbeFuU/0Ht7rvvvor333333TVtb2pq6pSxiYkJ7d69W7t27So6TRK/P/670rZLj6NK4sdYaV0z9VXu+JyYmCj7H55q6yqtJz/nrrvuKlqv9HYt26qH2dQ3n1S7r+q9T2cMYDP7opmNmtnosWPHan6Aw4cPFw7QEILypzwmJyd16NChadetpJqQxuzNdFqqmueomsc4dOiQDh8+POPjzVRL6XFUSaVjbKa+ys2drvZq64pvMz4n/m6h3O1atlUPs6lvPql2X9V7n84YwCGEB0MIvSGE3u7u7pofYNWqVUokcp/1mZnMTFLu3ODq1aunXbeSZDL5wYn/BS2F8ZNtH1U6ndaOHTsKP6hd/jmaTjXPUTWPsXr1aq1atWrGx5upltLjqJJKx9hMfZWbO13t1dYV32Z8Tv58d17p7Vq2VQ+zqW8+qXZf1Xuf1v0URH9/vxYsyD1Ma2urWltbJeU+qd+wYcO061YyPDx85gtFwQ033FDx/q1bt9a0vZaWllPGWltbtWHDBvX39xeOidL7478rbbv0OKokfoyV1jVTX+WOz9bW1rLBXW1dpfXk5wwMDBStV3q7lm3Vw2zqm0+q3Vf13qd1D+Curi6tWbNGZqa1a9cWltesWXPKVzri6yaTybLbSyaTNX0N7bHHHjud8j90UqmU1q9fX7T/48upVEorV64sesWTv79cECUSCV155ZUys6I5a9euVVdXV+E5L61h7dq1MjP19fUV5qVSqcJyMpmc9jiqJH6MrVu3rujVzUxfQ4vPTaVShWO6r6+vqPZa6opvMz4nnU4X9V3N17ym21Y9zKa++aTafVXvfTonf4jR39+vSy65pPCKJ79cad3h4WG1tbXprLPOKnoVxKvfmbW0tJyy36TigOzu7lZPT09hrLOzU+3t7YVXMkNDQ1qwYIGWLl2qoaEhtbe3q62trXD/wMCAFi5cqAsvvFBDQ0Pq6OjQli1b1N7erp6eHp1//vmScq8q88/pwMCALrroIi1btqzo+e/v79eyZcvU09NTqCF+nAwMDKijo0MDAwOF5aGhoYrHUSXxbW/ZsqVQZy1zBwYGio7pfF/x8dnUExfv+3S3VQ+zqW8+qXZf1XOfzsn3gM+E/Dca4ud1q/0ecLm5ADBX3L4HDAAojwAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJwQwADghgAHACQEMAE4IYABwQgADgBMCGACcEMAA4IQABgAnBDAAOCGAAcAJAQwATghgAHBCAAOAEwIYAJwQwADghAAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJwQwADghgAHACQEMAE4IYABwkvAuoFrpdNplLgDUS8ME8MaNG13mAkC9cAoCAJwQwADghAAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJwQwADghgAHACQEMAE4IYABwQgADgBMCGACcEMAA4IQABgAnBDAAOCGAAcAJAQwATghgAHBCAAOAEwIYAJwQwADghAAGACcEMAA4IYABwAkBDABOCGAAcEIAA4ATAhgAnBDAAOCEAAYAJwQwADghgAHACQEMAE4IYABwQgADgJPGD+CpSbW8P6725/ar5f23vasBgKolvAs4Hel0Wq+99pokafHi8ySdp3Q67VsUAFTJQghVr9zb2xtGR0frWA4ANB8zGwsh9JaON/4pCABoUAQwADghgAHACQEMAE4IYABwQgADgBMCGACcEMAA4IQABgAnBDAAOCGAAcAJAQwATghgAHBCAAOAEwIYAJwQwADghAAGACcEMAA4IYABwAkBDABOavqfcprZMUkv1a+cWTlX0lveRdRJM/cmNXd/9NaY6tXbkhBCd+lgTQE8H5nZaLn/22gzaObepObuj94a01z3xikIAHBCAAOAk2YI4Ae9C6ijZu5Nau7+6K0xzWlvDX8OGAAaVTO8AgaAhkQAA4CThg5gM1tjZs+bWcbMbvOupxwz+4SZHTGzZ83sGTPbHI2fY2aHzOyF6HdnbM7tUU/Pm9mfxcZXmNlPo/vuNzOLxs8ys+9G40+YWWqOe2wxs/8ys71N2NvHzex7ZvZc9Bxe1iz9mdmN0TH5tJl9x8zaGrU3M/ummb1pZk/HxuakFzPrjx7jBTPrr6nwEEJD/khqkfQLST2SPiLpqKRl3nWVqXORpE9Hy2dL+rmkZZL+TtJt0fhtkr4ULS+LejlL0tKox5boviclXSbJJB2QtDYa/xtJX42WPy/pu3Pc402S/knS3uh2M/W2S9JfRcsfkfTxZuhP0mJJL0pqj27/i6RrG7U3SX8q6dOSno6N1b0XSedI+u/od2e03Fl13XN5MJ/hHX6ZpEdjt2+XdLt3XVXU/bCk1ZKel7QoGlsk6flyfUh6NOp1kaTnYuPXSHogvk60nFDuL3lsjvq5QNIPJX1WHwRws/T2UeVCykrGG74/5QL4lSg4EpL2SrqikXuTlFJxANe9l/g60X0PSLqm2pob+RRE/gDKezUam7eity2XSnpC0nkhhDckKfr9W9Fq0/W1OFouHS+aE0KYlPQrSV11aeJU90m6VdLJ2Fiz9NYj6Zikf4hOsXzdzDrUBP2FEF6T9GVJL0t6Q9KvQgg/UBP0FjMXvZxWDjVyAFuZsXn7nTozS0r6N0k3hBDerbRqmbFQYbzSnLoys3WS3gwhjFU7pczYvOwtklDube1XQgiXSnpPubey02mY/qLzoeuVewt+vqQOM/tCpSllxuZlb1U4k72cVo+NHMCvSvpE7PYFkl53qqUiM2tVLny/HUL4fjT8P2a2KLp/kaQ3o/Hp+no1Wi4dL5pjZglJH5P09pnv5BR/JOkqM8tK+mdJnzWzb6k5ess/9qshhCei299TLpCbob9Vkl4MIRwLIUxI+r6kP1Rz9JY3F72cVg41cgD/WNKFZrbUzD6i3InxR5xrOkX0Keo3JD0bQtgeu+sRSflPTPuVOzecH/989KnrUkkXSnoyegv1f2b2mWibG0rm5Ld1taQfheiEVD2FEG4PIVwQQkgpt/9/FEL4QjP0JkkhhF9KesXMPhkNfU7Sz9Qc/b0s6TNmtjCq6XOSnlVz9JY3F708KukKM+uM3lVcEY1Vp94n++v5I6lPuW8V/ELSVu96pqnxj5V7S/KUpJ9EP33KnT/6oaQXot/nxOZsjXp6XtGnsNF4r6Sno/t26oO/ZGyT9K+SMsp9itvj0Ofl+uBDuKbpTdLvSRqNnr9/V+6T7qboT9KwpOeiuv5RuW8FNGRvkr6j3LnsCeVelf7lXPUi6S+i8YykP6+lbv4UGQCcNPIpCABoaAQwADghgAHACQEMAE4IYABwQgDDjZml4levqmL9h8zs6nrWBMwlAhgAnBDA8JYws11m9pTlrru70Mz+1sx+HF2n9sH8NVnjplvHzB4zsy+Z2ZNm9nMz+5NovMXMvhxd6/UpM9sYja8ws8fNbMzMHs3/6SowFwhgePukpAdDCMslvavcdVd3hhB+P4RwsaR2SevKzKu0TiKE8AeSbpA0GI19UbkLz1waPda3o2t0jEi6OoSwQtI3Jd19xjsEppHwLgAfeq+EEP4zWv6WpE2SXjSzWyUtVO56tc9I2lMyb2WFdfIXPBpT7hqxUu7iM18NuUsJKoTwtpldLOliSYeiF9Atyv05KzAnCGB4K/1b+CDp7yX1hhBeMbMh5f4Ov8DM2mZY5zfR7yl9cIxbmccySc+EEC473SaA2eAUBLz9tpnlA/AaSf8RLb8VXUO53Lce2qpYp9QPJP11dClBmdk5yl2IpTv/+GbWama/O8s+gJrxChjenpXUb2YPKHfVqq8od8Wxn0rKKnfZ0SIhhP81s69VWqeMr0v6HUlPmdmEpK+FEHZGX2u738w+pty/h/uUO50B1B1XQwMAJ5yCAAAnBDAAOCGAAcAJAQwATghgAHBCAAOAEwIYAJz8P59oTKGQbK6gAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the boxplot of balance variable.\n",
    "\n",
    "sns.boxplot(inp1.balance)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x144 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the boxplot of balance variable after scaling in 8:2.\n",
    "plt.figure(figsize=[8,2])\n",
    "sns.boxplot(inp1.balance)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.50      448.0\n",
       "0.70     1126.0\n",
       "0.90     3576.0\n",
       "0.95     5769.0\n",
       "0.99    13173.4\n",
       "Name: balance, dtype: float64"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#print the quantile (0.5, 0.7, 0.9, 0.95 and 0.99) of balance variable\n",
    "inp1.balance.quantile([0.5, 0.7, 0.9, 0.95, 0.99])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=8e8344a8-5fd6-4df3-be38-8d00cea646c8 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('8e8344a8-5fd6-4df3-be38-8d00cea646c8').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "      <th>balance</th>\n",
       "      <th>day</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>351.000000</td>\n",
       "      <td>351.000000</td>\n",
       "      <td>351.000000</td>\n",
       "      <td>351.000000</td>\n",
       "      <td>351.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>351.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>45.341880</td>\n",
       "      <td>70008.547009</td>\n",
       "      <td>24295.780627</td>\n",
       "      <td>16.022792</td>\n",
       "      <td>2.749288</td>\n",
       "      <td>188.516129</td>\n",
       "      <td>0.555556</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>12.114333</td>\n",
       "      <td>34378.272805</td>\n",
       "      <td>12128.560693</td>\n",
       "      <td>8.101819</td>\n",
       "      <td>3.036886</td>\n",
       "      <td>118.796388</td>\n",
       "      <td>1.784590</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>23.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>15030.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>35.000000</td>\n",
       "      <td>50000.000000</td>\n",
       "      <td>17074.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>96.250000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>44.000000</td>\n",
       "      <td>60000.000000</td>\n",
       "      <td>20723.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>167.500000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>55.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>26254.000000</td>\n",
       "      <td>21.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>246.500000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>84.000000</td>\n",
       "      <td>120000.000000</td>\n",
       "      <td>102127.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>589.000000</td>\n",
       "      <td>23.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "              age         salary        balance         day    campaign  \\\n",
       "count  351.000000     351.000000     351.000000  351.000000  351.000000   \n",
       "mean    45.341880   70008.547009   24295.780627   16.022792    2.749288   \n",
       "std     12.114333   34378.272805   12128.560693    8.101819    3.036886   \n",
       "min     23.000000       0.000000   15030.000000    1.000000    1.000000   \n",
       "25%     35.000000   50000.000000   17074.000000    9.000000    1.000000   \n",
       "50%     44.000000   60000.000000   20723.000000   18.000000    2.000000   \n",
       "75%     55.000000  100000.000000   26254.000000   21.000000    3.000000   \n",
       "max     84.000000  120000.000000  102127.000000   31.000000   31.000000   \n",
       "\n",
       "            pdays    previous  \n",
       "count   62.000000  351.000000  \n",
       "mean   188.516129    0.555556  \n",
       "std    118.796388    1.784590  \n",
       "min     31.000000    0.000000  \n",
       "25%     96.250000    0.000000  \n",
       "50%    167.500000    0.000000  \n",
       "75%    246.500000    0.000000  \n",
       "max    589.000000   23.000000  "
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the inp1 dataset for balance variable to be greater than 15000 in inp1.\n",
    "inp1[inp1.balance>15000].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 6, Standardising values "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Checklist for data standardization exercises:\n",
    "- **Standardise units**: Ensure all observations under one variable are expressed in a common and consistent unit, e.g., convert lbs to kg, miles/hr to km/hr, etc.\n",
    "- **Scale values if required**: Make sure all the observations under one variable have a common scale.\n",
    "- **Standardise precision** for better presentation of data, e.g., change 4.5312341 kg to 4.53 kg.\n",
    "- **Remove extra characters** such as common prefixes/suffixes, leading/trailing/multiple spaces, etc. These are irrelevant to analysis.\n",
    "- **Standardise case**: String variables may take various casing styles, e.g., UPPERCASE, lowercase, Title Case, Sentence case, etc.\n",
    "- **Standardise format**: It is important to standardise the format of other elements such as date, name, etce.g., change 23/10/16 to 2016/10/23, “Modi, Narendra” to “Narendra Modi\", etc."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Duration variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    261 sec\n",
       "1    151 sec\n",
       "2     76 sec\n",
       "3     92 sec\n",
       "4    198 sec\n",
       "5    139 sec\n",
       "6    217 sec\n",
       "7    380 sec\n",
       "8     50 sec\n",
       "9     55 sec\n",
       "Name: duration, dtype: object"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1.duration.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count       45161\n",
       "unique       2646\n",
       "top       1.5 min\n",
       "freq          138\n",
       "Name: duration, dtype: object"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the duration variable of inp1\n",
    "inp1.duration.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "#convert the duration variable into single unit i.e. minutes. and remove the sec or min prefix.\n",
    "inp1.duration=inp1.duration.apply(lambda x: float(x.split()[0])/60 if x.find(\"sec\")> 0 else float(x.split()[0]) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    45161.000000\n",
       "mean         4.302774\n",
       "std          4.293129\n",
       "min          0.000000\n",
       "25%          1.716667\n",
       "50%          3.000000\n",
       "75%          5.316667\n",
       "max         81.966667\n",
       "Name: duration, dtype: float64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#describe the duration variable\n",
    "inp1.duration.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Session- 3, Univariate Analysis "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 2, Categorical unordered univariate analysis "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Unordered data do not have the notion of high-low, more-less etc. Example:\n",
    "- Type of loan taken by a person = home, personal, auto etc.\n",
    "- Organisation of a person = Sales, marketing, HR etc.\n",
    "- Job category of persone.\n",
    "- Marital status of any one.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Marital status "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "married     0.601957\n",
       "single      0.282943\n",
       "divorced    0.115099\n",
       "Name: marital, dtype: float64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the percentage of each marital status category. \n",
    "inp1.marital.value_counts(normalize= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the bar graph of percentage marital status categories\n",
    "inp1.marital.value_counts(normalize= True).plot.barh()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Job  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "blue-collar      0.215274\n",
       "management       0.209273\n",
       "technician       0.168043\n",
       "admin.           0.114369\n",
       "services         0.091849\n",
       "retired          0.050087\n",
       "self-employed    0.034853\n",
       "entrepreneur     0.032860\n",
       "unemployed       0.028830\n",
       "housemaid        0.027413\n",
       "student          0.020770\n",
       "unknown          0.006377\n",
       "Name: job, dtype: float64"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the percentage of each job status category.\n",
    "inp1.job.value_counts(normalize= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaoAAAD4CAYAAAC9vqK+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgIklEQVR4nO3de5hcVZ3u8e9LQC4hF5HABBQbkTsJkVwkEAI4gaOgIBqNM6hEwAAeQT2DTGaYowgiYHiO3C8hgwERRBCYAErCLQl3kkCuSMABPAhMAMVICBNC8ps/9iqyU1R3V3VXV+/qvJ/n6aer915r7VX7Kfg9a9fOfhURmJmZFdVG3T0BMzOztrhQmZlZoblQmZlZoblQmZlZoblQmZlZoW3c3RPoabbeeutoaWnp7mmYmTWVefPmvR4RAyrtc6Gqs5aWFubOndvd0zAzayqS/tjaPl/6MzOzQnOhMjOzQnOhMjOzQvN3VHW26KXltEy8s912L5x7eANmY2bW/JpyRSVpvKRLunseZmbW9ZqyUJmZ2YajEIVKUoukxbm/T5V0hqSZks6T9LikZyQdUKHv4ZIekbS1pKmSLpL0sKTnJI1NbSRpkqTFkhZJGpe2XybpiPT6VklXp9fHSfpxmtfvJV0laYmkGZI2b8xZMTMzKEihasfGETEC+C7ww/wOSUcBE4HDIuL1tHkgMAr4LHBu2vYFYAiwNzAGmCRpIDAbKBW/7YE90utRwAPp9c7ApRGxJ/BX4IvlE5Q0QdJcSXPXrFzemfdqZmZlmqFQ3ZJ+zwNactsPBv4ZODwi3shtvy0i1kbEU8C2adso4IaIWBMRy4BZwHCyYnSApD2Ap4BlqYCNBB5OfZ+PiPmtzAGAiJgcEcMiYlivLfp16s2amdn6ilKo3mX9uWyWe70q/V7D+ncpPgf0AXYpG2tV7rXKfq8nIl4CPgh8mmx19QDwZWBFRLxZYbzyOZiZWRcrSqFaBmwj6UOSNiW7bNeeP5Jd0rtW0p7ttJ0NjJPUS9IAYDTweNr3CNllxVKhOpV1l/3MzKybFaJQRcRq4EzgMeAO4Okq+y0FjgZukrRTG01vBRYCC4D7gNMi4r/SvgfIvgf7A/AEsBUuVGZmhaGI6O459CjDhg0LP5TWzKw2kuZFxLBK+wqxojIzM2uNC5WZmRWaC5WZmRWaC5WZmRWaC5WZmRWaC5WZmRWaC5WZmRWaC5WZmRWan1tXZ9Um/HYFpwabWU/UlCsqSd+VtEUH+q3oxDHHS9quo/3NzKxjmrJQkT1EtuZC1UnjARcqM7MGK3yhktRb0p2SFqSE3h+SFYz7Jd2f2qzItR8raWp6vWNK/50j6ayycb+fti+U9KO0rWKib0oKHgb8UtJ8p/yamTVO4QsVWVbUyxGxd0TsBVwAvAwcHBEHt9P3QuDyiBgOlJ6WjqRDyZJ7R5Al/w6VNDrtfl+ib0TcDMwFjo6IIRHxdr3enJmZta0ZCtUiYIyk8yQdEBG1ZL3vD9yQXv8it/3Q9PMkWbTHbmQFCqpI9C3nKHozs65T+Lv+IuIZSUOBw4BzJM2o1Cz3erM29pUIOCcirlxvo9TC+xN9273MFxGTgckAmw7c2bkpZmZ1VPgVVbrTbmVEXAecD+wDvEkWQ1+yTNLukjYCjsptfwj4Snp9dG77dOBYSVumY2wvaZt2plJ+TDMza4DCr6iAQcAkSWuB1cBJwEjgd5JeSd9TTSRLBn4RWAxsmfp+B7he0neA35QGjIgZknYHHpEEsAL4KtkKqjVTgSskvQ2M9PdUZmaN4YTfOnPCr5lZ7Zzwa2ZmTcuFyszMCs2FyszMCs2FyszMCs2FyszMCs2FyszMCs2FyszMCs2FyszMCq0ZnkzRVLoz4bdaTgI2s2bSpSuqlO+0uCuPUW+StpN0cyv7Zkqq+C+nzcysa3hFVSYiXgbGdvc8zMws04jvqHpVSMwdIunRlK57q6QPwvorFklbS3ohvd5T0uMpXXehpJ3T9q/mtl8pqVfaviLlV82TdI+kEWns5yQdkdq0SHpA0hPpZ7/c9sXp9eaSfpWOeSNVRH6YmVl9NaJQvS8xF7gW+OeIGEwWjPjDdsY4EbgwIoaQRcL/KT39fBywf9q+hnVRHr2BmRExlCye48fAIWQRIGemNq8Ch0TEPmmciyoc9ySyiJHBwNnA0JreuZmZdVojLv2VJ+buBPSPiFlp2zXATe2M8QhwuqQPA7dExLOS/p6scMxJUR2bkxUfgHeAu9LrRcCqiFgtaRHrEns3AS6RNISsyO1S4bijSQUsIhZKWlhpcpImABMAevUd0M5bMTOzWjSiUJUn5vZvo+27rFvlvZfUGxHXS3oMOByYLul4spTeayLiXyqMszrW5ZesLc0hItZKKr3n7wHLgL3TMf+7lTm1m4PihF8zs67THf+OajnwhqQD0t9fA0qrqxdYd3ntvRsaJH0MeC4iLgKmAYOBe4GxpWReSVtJ+mgN8+gHvBIRa9McelVoM5t0OVHSXum4ZmbWQN31D36PIUvtXQgMYd33RucDJ0l6GNg6134csFjSfGA34NqIeAr4N2BGGuduYGANc7gMOEbSo2SX/d6q0OZyYMs0/mnA4zWMb2ZmdeCE3zpzwq+ZWe2c8GtmZk3LhcrMzArNhcrMzArNhcrMzArNhcrMzArNhcrMzArNhcrMzArNhcrMzArNeVR11gwJvyVO+jWzZuAVlZmZFVqPKVSSDpJ0Rxcf4wVJW7ff0szM6qXHFCozM+uZOl2o8tHt6e9TJZ2Rot/PS1Hxz5RiPST1kjRJ0pwU8X5C2n6QpFmSfp3anyvp6NR/kaSdUrupkq5IMfLPSPpshTltJem2NP6jkgZL2kjSs5IGpDYbSfpDirwfIOk3aU5zJO2f2nxI0gxJT0q6kiwDy8zMGqirV1QbR8QI4Lusi5s/DlgeEcOB4cA3Je2Y9u0NfAcYRJYRtUvqPwU4OTduC3AgWZDiFZI2Y30/Ap5MEfL/ShYLsha4jnVx9WOABRHxOnAh8LM0py+m45Hm/GBEfIIsB2uHSm9S0gRJcyXNXbNyedUnx8zM2tfVd/3dkn7PY10E/KHAYEmlYMR+wM5k8fFzIuIVAEn/CcxIbRYBB+fG/XUqPM9Keo4soypvFFnBISLuSyujfsDVwH8AFwDHAj9P7ccAe6RIe4C+kvqQRdF/IY1zp6Q3Kr1JJ/yamXWdehSqfHw85CLkWRdDvyZ3LAEnR8T0/CCSDmL92Pq1ub/Xls21vBiU/13pEl1ExIuSlkn6FPBJ1q2uNgJGRsTbZXOqNLaZmTVQPS79LQO2SauWTYH3fWdUZjpZiu8mAJJ2kdS7xmN+KX3HtBPwMWBp2f58hPxBwOsR8be0bwrZJcBfR8SatG0G8O1SZ0lDKozzGeCDNc7TzMw6qdMrqohYLelM4DHgeeDpdrpMIbsM+ISyJctrwOdrPOxSYBawLXBiRPx37rIdwBnAz1OE/ErgmNy+aWSX/H6e23YKcGlqvzFZgTqR7LuuGyQ9kY73/9ub2KDt+zHX/5DWzKxumi6KXtJU4I6IuLmD/YeR3ThxQF0nljiK3sysdm1F0W9Qj1CSNBE4iXXfTZmZWcE1XaGKiPGd6HsucG79ZmNmZl3NT6YwM7NCc6EyM7NCc6EyM7NCc6EyM7NCc6EyM7NCa7q7/oqumRJ+W+PkXzMrEq+ozMys0Lq8UEn6vKQ9uvo4ZmbWMzViRfV5oGKhktSpS4+d7d8sxzQz25B1qFBJ+mpK3p0v6cqU2rtC0tmSFqRU3W0l7QccAUxKbXdKyb8/kTQL+I6koSnZd56k6ZIGpmPMlHSBpIclLZY0Im0/Q9JkSTOAa9tI5z1D0tVpnOckndLW/NP2Fbk2Y9NzBUupwv9P0v3AeR05Z2Zm1jE1rw4k7Q6MA/ZPT06/jOzZeb2BRyPidEk/Bb4ZET+WNI3cQ2TTU877R8SBKepjFnBkRLwmaRxwNlmoIUDviNhP0miy0MO90vahwKiIeFvS9WQPmX1Q0g5kMSK7p3a7kQUu9gGWSroc+Hgr87+2nbe+CzAmFw2SPycTgAkAvfoOqPJMmplZNTpyGevvyQrFnFR0NgdeJUvovSO1mQcc0sYYN6bfu5IVn7vTWL2AV3LtbgCIiNmS+krqn7ZPy4UctpbOC3BnRKwCVkl6lSwWpLX5t+emSkUqzc8Jv2ZmXaQjhUrANRHxL+ttlE6NdZkh+UTfSt7KjbUkIka20q61JN+3ctvaSufNJwaX5lRx/hWOt1nZvrcwM7OG68h3VPcCYyVtAyBpK0kfbaP9m2SX3ipZCgyQNDKNtYmkPXP7x6Xto4DlEbG8whitpfN2ZP7LJO0uaSPgqHbGMTOzBqh5RRURT0n6N2BG+h/6auB/t9HlV8BV6WaGsWVjvSNpLHCRpH5pPhcAS1KTNyQ9DPRl3fdW5VpL5611/n8EJpJdvnwRWAxs2cb7qsgJv2Zm9VXYhF9JM4FTI6Kp4nKd8GtmVru2En79ZAozMyu0wv7j1Yg4qLvnYGZm3c8rKjMzKzQXKjMzKzQXKjMzKzQXKjMzKzQXKjMzK7TC3vXXrHpCwm+e037NrLt5RWVmZoVW10KVcpvGptcHSFqSMp82r+dx2jj+ivZbdWr8996fmZk1RleuqI4Gzo+IIeVPNjczM6tWu4VKUm9Jd6bk3sWSxrWWypvrczzwZeAHkn5ZYcxWE3YlnZfGvUfSiFxC7xGpzXhJ/yHpLklLJf2wwviSNCnNd1EKZETSLyQdmWv3S0lHKEsonpQSghdKOiE3ziWSnpJ0J7BNTWfXzMw6rZoV1aeBlyNi74jYC7gLuBgYGxFDyZJ3z853iIgpwDTg+xFxdH5fWULwELKcqFKb3sDMNO6bwI/JAhiPAs7MDTMi9RkCfElS+YMMv5D27U0WrDgpFdMpwDfSPPoB+wG/BY4jixEZDgwHvilpx3TcXYFBwDdT+/eRNEHSXElz16yslERiZmYdVc1df4uA8yWdRxaB8QZtp/K2p62E3XfICmHpuKtSXPwioCU3xt0R8WcASbcAo4D8I8tHATekRN5lkmYBwyNimqRLUxbVF4DfRMS7kg4FBue+f+oH7AyMzo3zsqT7Kr0hJ/yamXWddgtVRDwjaShwGHAOcDdtp/KuR9JHgNvTn1fQdsLu6lxK8FpSQm9ErJWUn2tryb/vHbaNKf2CbDX2FdZlXAk4OSKml839sApjm5lZA1XzHdV2wMqIuA44H/gkbafyriciXkw3VAyJiCuoPSG4kkNSv82BzwMPle2fDYxL3z0NIFsZPZ72TQW+m+ZWCmicDpwkaZM0p10k9U7jfCWNMxA4uMZ5mplZJ1Vz6W8Q2Xc8a8nScE8C3qX1VN42tZOwW60HyVZGHweurxCueCswElhAtiI6LSL+Kx1/maTfA7fl2k8hu7T4hLLrka+RFcBbgU+RXYZ8BphVwxzNzKwOCpvw2xpJ44FhEfHtDvbfgqzw7BMRdb/zwQm/Zma1c8JvImkM8DRwcVcUKTMzq7+me9ZfREwl+56pI33vAXao53zMzKxrbVArKjMzaz4uVGZmVmguVGZmVmguVGZmVmguVGZmVmguVGZmVmhNd3t60fW0KPqu5Jh7M6tGj11RSeov6Vu5v7eTdHMnx5xZIVLEzMy6UNMXqhRuWOl99AfeK1QR8XJEvC9Gvuyp7GZmVjBNWagktUj6vaTLgCeA/5tL5/1RanYusFNKEZ6U+ixO/cdLuknS7WQPx+0t6eo0xpOlFGBJm0v6VRr3RrLsLDMza6BmXk3sSpbWexswliz1V8A0SaOBicBeKUUYSS1l/UcCgyPiL5J+AtwXEcdK6g88Luke4ASyiJPBkgaTFcX3kTQBmADQq++Aer5HM7MNXlOuqJI/RsSjwKHp50myQrIbWTpve+6OiL+k14cCEyXNB2YCm5E9E3A0cB1ARCwEFlYaKCImR8SwiBjWa4t+HX5DZmb2fs28onor/RZwTkRcmd9ZYQXVWv/SGF+MiKVlY4ATfs3MulUzr6hKpgPHStoSQNL2KT34TaBPDWOcnEITkfSJtH02WWw9kvYCBtdz4mZm1r6mL1QRMQO4HnhE0iLgZqBPRPwZeEjSYkmT2hnmLGATYGG64eKstP1yYEtJC4HTWBdnb2ZmDdJ0Cb9F54RfM7PaOeHXzMyalguVmZkVmguVmZkVmguVmZkVmguVmZkVmguVmZkVmguVmZkVmguVmZkVWjM/66+QnPBrbXGqsVntNpgVlaQzJY3p7nmYmVltetSKStLGEfFupX0R8YNGz8fMzDqvkCuqlLh7p6QF6aGy4yQNlTRL0jxJ0yUNTG1nSvqJpFnA6ZJeKEXTS9pC0ouSNpE0VdLYtH24pIfT+I9L6iOpV0oCLiUFn5DaDpQ0OyUFL5Z0QLedGDOzDVBRV1SfBl6OiMMBJPUDfgccGRGvSRoHnA0cm9r3j4gDU9t9gAOB+4HPAdMjYnVK8EDSB4AbgXERMUdSX+Bt4DhgeUQMl7Qp2ZPXZwBfSGOcLakXsEX5ZJ3wa2bWdYpaqBYB50s6D7gDeAPYC7g7FZxewCu59jeWvR5HVqi+AlxWNvauwCsRMQcgIv4GIOlQYHBp1QX0I0sKngNcLWkT4LaImF8+2YiYDEwG2HTgzn4cvZlZHRWyUEXEM5KGAocB5wB3A0siYmQrXfJpvdOAcyRtBQwF7itrKyqn9go4OSKmv2+HNBo4HPiFpEkRcW1Nb8jMzDqsqN9RbQesjIjrgPOBTwIDJI1M+zeRtGelvhGxgizg8ELgjohYU9bkaWA7ScPTWH0kbUyW8ntSWjkhaZf0XdlHgVcj4irg34F96v1+zcysdYVcUQGDgEmS1gKrgZOAd4GL0vdVGwMXAEta6X8jcBNwUPmOiHgnfcd1saTNyb6fGgNMAVqAJ1Ik/WvA59MY35e0GlgBfL0eb9DMzKrjhN86c8KvmVntnPBrZmZNy4XKzMwKzYXKzMwKzYXKzMwKzYXKzMwKzYXKzMwKzYXKzMwKzYXKzMwKrahPpmhaTvi1ZuCkYWsmPW5FJWm8pEtq7PNbSf27aEpmZtYJXlEBEXFYd8/BzMwqa7oVlaTbUsrvkhRYiKRvSHompfzun2s7VdLlku6X9JykAyVdLen3kqbm2r0gaWtJLWnfVWn8GenBtWZm1k2arlABx0bEUGAYcIqk7YEfkRWoQ4A9ytp/EPgU8D3gduBnwJ7AIElDKoy/M3BpROwJ/BX4YnsTkjRB0lxJc9esXN6hN2VmZpU1Y6E6RdIC4FHgI8DXgJkR8VpEvMP6ab8At0f2iPhFwLKIWBQRa8kiQloqjP98LsV3Xitt1hMRkyNiWEQM67VFv468JzMza0VTFSpJB5FlR42MiL2BJ8mCENvKKlmVfq/NvS79Xek7unybNa20MTOzBmmqQgX0A96IiJWSdgP2BTYHDpL0oZTO+6VunaGZmdVVs60W7gJOlLQQWEp2+e8V4AzgkfT6CaBXvQ8s6USAiLii3mObmVnrnPBbZ074NTOrnRN+zcysablQmZlZoblQmZlZoblQmZlZoblQmZlZoblQmZlZoblQmZlZoblQmZlZoTXbkykKzwm/Zj2b05Ebr2ErKkn9JX2rg32nShpbY58pksojP/L7j5A0sSPzMTOzxmnkpb/+QIcKVUdExPER8VQb+6dFxLmNmo+ZmXVMIwvVucBOkuZLmiTp+5LmSFoo6UelRpK+nrYtkPSLXP/Rkh5OSb1jU9uDJM2UdLOkpyX9UpLSvpmShqXXn5b0RBrz3rRtvKRL0uvPSXpM0pOS7pG0bdp+RkoEnpmOe0pjTpWZmZU08juqicBeETFE0qHAWGAEIGCapNHAn4HTgf0j4nVJW+X6DwRGAbsB04Cb0/ZPkCX2vgw8RJb0+2Cpk6QBwFXA6Ih4vmzMkgeBfSMiJB0PnAb8U9q3G3Aw0AdYKunyiFjdyXNhZmZV6q6bKQ5NP0+mv7cki4DfG7g5Il4HiIi/5PrclpJ5nyqteJLHI+JPAJLmkyXyPpjbvy8wOyKerzBmyYeBGyUNBD4APJ/bd2dErAJWSXoV2Bb4U76zpAnABIBefQdU8/7NzKxK3XV7uoBzImJI+vl4RPx72t5a7kg+eVetbK+UyNvWmCUXA5dExCDgBGCzGsZ3FL2ZWRdqZKF6k+zyGcB04FhJWwJI2l7SNsC9wJclfShtr3SZrlaPAAdK2rGNMfsBL6XXx9ThmGZmVicNu/QXEX+W9JCkxcDvgOuBR9K9DyuAr0bEEklnA7MkrSG7NDi+k8d9LV2au0XSRsCrwCFlzc4AbpL0Ellq8I6dOaaZmdWPE37rzAm/Zma1c8KvmZk1LRcqMzMrNBcqMzMrNBcqMzMrNBcqMzMrNBcqMzMrNBcqMzMrNBcqMzMrNCf81pkTfs2sp+nuVGOvqKokqUXSP3b3PMzMNjQuVNVrAVyozMwarOZClVYWT0uaImlxStUdkx44+6ykEenn4ZSY+7CkXVPf8ZJukXRXavvT3LiXS5oraUlZ4u9h6XgPSrpI0h1pe++UvjsnHefI3DFuk3S7pOclfVvS/0ltHi09PV3STmke8yQ9IGm3tH1qOs56acJkCcUHpITi73X0hJuZWW06uqL6OHAhMJgsAfcfydJ3TwX+FXiaLFH3E8APgJ/k+g4BxgGDgHGSPpK2n54eSDiYLJZjsKTNgCuBz0TEKCCfSng6cF9EDCdL4J0kqXfat1ea0wjgbGBlmssjwNdTm8nAyRExNM37stzYpTThz5IVKMgSih9I+Vk/q/F8mZlZB3X0ZornI2IRgKQlwL0pxn0R2SWyfsA1knYmCy3cJNf33ohYnvo+BXwUeJEsh2pCmtNAYA+yQvpcKZ0XuIGUpEuWEHyEpFPT35sBO6TX90fEm8CbkpYDt6fti4DBKQdrP7Joj9K8Ns3NsbU04Yqc8Gtm1nU6Wqjyqbdrc3+vTWOeRVYsjpLUAsxspe8aYOMUangqMDwi3pA0lazw5JN8ywn4YkQsXW+j9Mkq5rcR8NeIGFLF+2trDkCW8Eu2QmPTgTs7N8XMrI666maKfGLu+Cra9wXeApanFcxn0vangY+lYgfZJcOS6cDJSksiSZ+odnIR8TfgeUlfSn0lae92uuUTis3MrEG6qlD9FDhH0kNAr/YaR8QCsjTfJcDVwENp+9vAt4C7JD0ILAOWp25nkV1SXJhSg8+qcY5HA8dJWpCOe2Q77RcC70pa4JspzMwap/AJv5K2jIgVaeV0KfBskW9mcMKvmVntmj3h95uS5pOtevqR3QVoZmYbiMI/Qimtngq7gjIzs67VDCsqMzPbgLlQmZlZoblQmZlZoblQmZlZoblQmZlZoblQmZlZoRX+9vRm44RfM9sQdWUKsFdUZmZWaA0rVClwcXGF7TMlVXxsRhfP56BcCON4SZc0eg5mZtY+r6g6QJIvmZqZNUijC9XGkq6RtFDSzZK2yO+UtCL3emzKpULSAEm/SbHzcyTtX2lwScNThPwCSY9L6iNpM0k/l7QoxdEf3NYEJX1O0mOp7T2l4ERJZ0iaLGkGcG1nT4SZmVWn0SuDXYHjIuIhSVeTRXhU40LgZxHxoKQdyLKods83kPQB4EZgXETMkdQXeBv4DkBEDJK0GzBD0i5tHOtBYN+UWHw8cBrwT2nfUGBUih/JH9sJv2ZmXaTRherFiHgovb4OOKXKfmOAPXKx8X0l9Ulx8yW7Aq9ExBx4LxwRSaOAi9O2pyX9EWirUH0YuFHSQOADwPO5fdPKi1Qa1wm/ZmZdpNGX/sr/J97W35vlXm8EjIyIIeln+4h4U9J0SfMlTSGLjK9UJNqNki9zMXBJRAwCTiibx1s1jmVmZp3U6EK1g6SR6fU/kF1my1smaXdJGwFH5bbPAL5d+kPSEICI+F+pcB1PFlu/naThqU2fdNPDbLI0X9Ilvx2ApW3MsR/wUnp9TO1v0czM6qnRl/5+Dxwj6UrgWeBy4HO5/ROBO4AXgcXAlmn7KcClkhaSzXk2cGJ+4Ih4R9I44GJJm5N9PzUGuAy4QtIi4F1gfESsyl1GLHcGcJOkl4BHgR1reYODtu/H3C78h29mZhuawkfRNxtH0ZuZ1a7Zo+jNzGwD5kJlZmaF5kJlZmaF5u+o6kzSm7R9V6GtszXwendPogn4PFXH56k6RT1PH42Iik9M8DPr6m9pa18I2vokzfW5ap/PU3V8nqrTjOfJl/7MzKzQXKjMzKzQXKjqb3J3T6CJ+FxVx+epOj5P1Wm68+SbKczMrNC8ojIzs0JzoTIzs0JzoaqBpE9LWirpD5ImVtgvSRel/Qsl7VNt356kk+fphZTGPF9Sj35oYhXnaTdJj0haJenUWvr2JJ08T/48rdt/dPrvbWFKQt+72r7dLiL8U8UP0Av4T+BjZIGKC4A9ytocBvyOLANrX+Cxavv2lJ/OnKe07wVg6+5+HwU5T9sAw4GzgVNr6dtTfjpznvx5et952g/4YHr9mWb6/5NXVNUbAfwhIp6LiHeAXwFHlrU5Erg2Mo8C/VNScDV9e4rOnKcNSbvnKSJejSyxenWtfXuQzpynDUk15+nhiHgj/fkoWZp5VX27mwtV9bYny8kq+VPaVk2bavr2FJ05T5ClNM+QNE/ShC6bZffrzGfCn6fq+fNU2XFkVzU60rfh/Ail6lVKWiy/t7+1NtX07Sk6c54A9o+IlyVtA9wt6emImF3XGRZDZz4T/jxVz5+n8obSwWSFalStfbuLV1TV+xPwkdzfHwZerrJNNX17is6cJyKi9PtV4FayyxI9UWc+E/48Vcmfp/VJGgxMAY6MiD/X0rc7uVBVbw6ws6QdJX0A+AowrazNNODr6a62fYHlEfFKlX17ig6fJ0m9JfUBkNQbOBRY3MjJN1BnPhP+PFXBn6f1z5OkHYBbgK9FxDO19O1uvvRXpYh4V9K3gelkd8lcHRFLJJ2Y9l8B/JbsjrY/ACuBb7TVtxveRpfrzHkCtgVulQTZZ/P6iLirwW+hIao5T5L+DpgL9AXWSvou2d1Yf/Pnqf3zRBZn4c8T7/139wPgQ8Bl6Zy8GxHDmuH/T36EkpmZFZov/ZmZWaG5UJmZWaG5UJmZWaG5UJmZWaG5UJmZWaG5UJmZWaG5UJmZWaH9DzLB+pC2w9zqAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the bar graph of percentage job categories\n",
    "inp1.job.value_counts(normalize= True).plot.barh()\n",
    "plt.plot()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 3, Categorical ordered univariate analysis "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ordered variables have some kind of ordering. Some examples of bank marketing dataset are:\n",
    "- Age group= <30, 30-40, 40-50 and so on.\n",
    "- Month = Jan-Feb-Mar etc.\n",
    "- Education = primary, secondary and so on."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Education"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "secondary    0.513275\n",
       "tertiary     0.294192\n",
       "primary      0.151436\n",
       "unknown      0.041097\n",
       "Name: education, dtype: float64"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the percentage of each education category.\n",
    "inp1.education.value_counts(normalize= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAARUAAADnCAYAAAAww8JEAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgRUlEQVR4nO3deXxcZdn/8c/VpPuSLrQ0XehQKLRQlrYsLRQoyINCVBZFRPQJoiyCIm44Px7RERXj/nvpT3xQHwUFRQQBZVRAoOyLbO3QJuxhL9A2maRt2ixz/f64Tx5CSZNJcmbumXOu9+s1r8x6zjdtcuU+59yLqCrGGBOWYb4DGGOixYqKMSZUVlSMMaGyomKMCZUVFWNMqKyoGGNCZUXFGBMqKyrGmFBZUTHGhMqKijEmVFZUjDGhsqJijAmVFRVjTKisqBhjQmVFpYyIyAoRudl3DmP6YkUlwkSk0ncGEz9WVAZARMaKSFpEVonIkyJyiogsEZG7RORREblFRKqD9+4uIv8K3vuYiOwmzg+Cz2ZE5JTgvStEZKWIXCciDSJytYhI8Nr7gufuBU7qkeUgEblfRB4Pvu4ZPH+6iPxZRP4G3CoivxeR43t87moR+WAx/91MzKiq3fK8AR8CftXjcRVwPzA1eHwK8Jvg/kPAicH9UcCY4PO3ARXAzsBLQDWwAsgCs3CF/gFgefC5l4F5gADXAjcH25wAVAb3jwauD+6fDrwCTA4eHwHc2CPvC92fs5vdCnGz5vHAZIAfisj3gJuBJmAhcFvQsKgAXheR8cBMVb0BQFW3AojIcuCPqtoFvCEidwEHAi3Aw6r6SvC+J4AEsAl4QVWfCZ6/CjgryFIFXCki8wAFhvfIeZuqbgz2fZeI/FxEpuFaOteramfo/zLGBKyoDICqPi0iS4DjgO/iWh1rVHVZz/eJyIQdbEL62Py2Hve7ePv/ZkeTCH8LuFNVTxSRBLCyx2ubt3vv74HTgI8CZ/SRwZghs3MqAyAiM4AtqnoV8EPgYGCqiCwLXh8uInuragvwioicEDw/UkTGAHcDp4hIhYhMBQ4HHu5jlw3AriKyW/D41B6vVQGvBvdP7yf6FcAFAKq6Jo9v1ZhBs5bKwOwD/EBEckAH8BmgE/ipiFTh/j3/L7AG+ARwuYhcErz3ZOAGYBmwCtcCuVBV14nI/N52pqpbReQsIC0i64F7cYdbAN/HHf58Ebijr9Cq+oaI1AM3DvYbNyZfompLdERd0ErKAItVNes7j4k2O/yJOBE5GncY9TMrKKYYrKVijAmVtVSMMaGyomKMCZVd/YmoRDI9BdcTd/fg63TcZeju23hgJDAi+Doc2ILr2dscfO15awY2AE8B9Y11NeuL9s2YsmLnVMpcIpneDddfZg/eLiDzgEkF3vV6oB5YG3ytxxWblwu8X1PirKiUmUQyPQ83nmdF8HWW10Dvtg64HfgXcFtjXc2r/bzfRIwVlRKXSKYTwDG8XURm+MwzCA0EBQZY2VhX0+I5jykwKyolKJFMT8aNeP44cIjnOGHqBB4ErgH+ZOdlosmKSolIJNOjgA/iBv4dyztHHUdRB3ALbrDjTY11Ndv6eb8pE1ZUPEsk04fjBgR+CDdHShytB34H/LKxruYp32HM0FhR8SCRTFfiBhh+GVjsOU6puQv4XmNdzT98BzGDY0WliBLJ9GjgTOCLwBzPcUrdQ8A3rbiUHysqRRAUk3OAC3Gd0Ez+HsYVl7/7DmLyY0WlgBLJdAVwLvBfuDlpzeD9G1dc0r6DmL5ZUSmQRDJ9CHAZsJ/vLBHzEPCZxrqax30HMb2zohKyRDK9E25WttPpe05aM3hduBn2vt5YV7PFcxazHSsqIUkk08NwJ2EvBSZ7jhMXjcC5djK3tFhRCUEimV4M/AI4yHeWmLoG+HxjXc2bvoMYKypDErROLga+js1N41sTcGFjXc2vfQeJOysqg5RIpqcBV+NWBzSl4y/A6Y11Na2+g8SVFZVBSCTTRwB/xC1ZakrPU8BJjXU1a30HiSMrKgOQSKYFuAj4Jm6JU1O6NgNnNNbVXOs7SNxYUclTcKn4KuC9vrOYAfkJ7lyLrR9dJFZU8pBIpvcF0pTeLGsmP/cAH2msq1nnO0gcWFHpR9AzNg1M9BzFDM3rwLGNdTWrfAeJOrsM2odEMn0sbhrEiZ6jmKGrBu5KJNPLfQeJOisqO5BIpj8K3ASM8Z3FhKYKuDWRTB/nO0iUWVHpRSKZ/gyuD0rUp3SMo9HAjYlk+mTfQaLKisp2Esn0xbjRxfZvE13DgT8kkulTfAeJIvvF6SGRTH8HuMR3DlMUlcDViWT6VN9Bosau/gQSyfQXgB/7zmGKrgs4pbGu5nrfQaLCigqQSKY/jpvN3eY/iac2YEVjXc3DvoNEQeyLSiKZfi9wM7ZYfdy9ARzcWFfzou8g5S7WRSWRTO8D3AeM953FlIQngUNtadahie2J2kQyPR3XQrGCYrotBP4UTFhuBimWRSVYMuOvwC6+s5iS8z7gp75DlLNYFhXcpMkH+g5hSta5iWT6875DlKvYnVNJJNMnADf4zmFKXhdwRGNdzX2+g5SbWBWVRDI9E1gFTPGdxZSF54D9G+tqNvkOUk5ic/gTTFL9O6ygmPztBvzId4hyE5uiAnwFOMp3CFN2zkok0zW+Q5STWBz+JJLpA4D7sVHHZnDWAfs01tWs9x2kHES+pZJIpscCf8AKihm86cB/+w5RLiJfVIAUMM93CFP2PpRIpj/hO0Q5iPThTyKZ3h1YA4zwncVEQhaY11hX85bvIKUs6i2VH2EFxYSnCrfErelDZFsqiWT6P4BbfecwkdMB7N1YV/OM7yClKpItlWBA2E985zCRNBz4nu8QpSySRQU4B9jbdwgTWSfaUh87FrmikkimJ+HWOjamkH7gO0CpilxRAS7GuuKbwltqy3z0LlInahPJ9GTgZWwBMFMczwF7NdbVtPsOUkqi1lI5Gysopnh2A07zHaLURKaoJJLp4cBnfecwsfMF3wFKTWSKCnAqMMN3CBM7+wR9okwgSkXF/mIYX77kO0ApicSJ2kQyfRRwu+8cJrYU2NN62TpRaanYXwrjk+AuEhgi0FJJJNN7AA3YkqXGrw3AzMa6mm2+g/gWhZbKJ7CCYvybAlhnOKJRVE71HcCYgE3iRJkf/iSS6YOBB33nMCbQAUxtrKvJ+g7iU7m3VKyVYkrJcOA43yF8K/eicpLvAMZs53jfAXwr28OfRDK9BHjEdw5jttOCOwSK7SDDcm6pnOA7gDG9mEDMF60r56IS+2amKVkn+A7gU1ke/iSS6WnAG75zGLMDr+M6wpXfL1cIyrWlssx3AGP6UA0s9h3Cl8p83iQie+AWOJ/T8zOq6uvY0YqKKXUHAY/6DuFDXkUF+DNuLdlfAV2Fi5O3pb4DGNOPA3wH8CXfotKpqr8oaJI8JZLpSuBA3zmM6Udsf0bzPafyNxE5V0SqRWRy962gyXZsX2weWlP69kok06N9h/Ah35ZKbfD1Kz2eU2BuuHHyYudTTDmoABYB9/sOUmx5FRVV3bXQQQbAioopFwdgRaV3IjIc+AxwePDUSuByVe0oUK6+xPZY1ZSdWP6s5nv48wvcCMzLgsefCJ77dCFC7UgimRYgUcx9GjMEsbwClFePWhFZpar79fdcoSWS6WrgtWLu05gh6ARGxK1nbb5Xf7pEZLfuByIyFz/9VeZ42Kcxg1UJTPMdotjyPfz5CnCniDyPmw92DvDJgqXasV087NOYoZhBzMap5Xv153YRmQfsiSsqDarqY9ZwKyqm3MwAHvcdopj6LCoicpSq3iEi28+wtpuIoKp/KWC23tjhjyk3sVuKt7+WyhHAHcAHenlNgWIXFWupmHJjRaUnVf1GcPcSVX2h52si4qNDnLVUTLmJXVHJ9+rP9b08d12YQfI01cM+jRmK2BWV/s6pzAf2Bqq2O68yARhVyGA7MNzDPo0Zium+AxRbf+dU9gTeD0zknedVWoEzC5SpL1ZUTLmJ3Yj6/s6p3ATcJCLLVPWBImXqS779aowpFbH7mc33G35cRM7DHQr972GPqp5RkFQ7Zi0VU25i9zOb74na3+OODd8L3AXMwh0CFVvs/oNM2YtdSyXfAYWPq+oiEVmtqvsGUyHcUsyJr4MRyrli7S8KxtLWurM0NVXLxpYZsn7LLHmrfaZs6Kxmg+wk2cpJsmnkWNrGjaBj/KmjZr+w9Em2Hvh0buxOrbm5oFbAQ6Ay7LWF9Wv28Z2jmPKtot3zpjSLyEJgHcWfgiD2P+Rjads0TZqbqmVDy0xZv2WmrN86g/Vd1bJRpklz5UTZNGocbWNG0lFVQW6yCOOB8flse8rELc9eeczoo688RhjZPmzzgU9r/YqMbt7zFZ0+opM9xA3PMAOluSbfEYot36LySxGZBHwN+CswDvh6wVL1LnLNyDG0bZ4mzRuny8aWWbJ+y0zWb5sp67uqZSNTpblikrSOGsfWsSNp7y4S43D/9qG7oKl51v1j3JSq20bI2HsXygH3LnSvVW3W9cvX6DPL1+Q657zJrpU5ZhUiQ0T5mMjMq7JZoTCRTFfg/oNK9i/maLZtmSZNG6tlQ8tMNmyeKd1FYgNTpblykmwaOY62MaPeLhIlNTHy0jmz1mweNmzv/t5XvUFfWpHJvbi0QSt3bmKPYTClGPnK1OoFDfVFnXfIt3zPqVwKfF9Vm4PHk4AvqerXChvvnRLJdBbX8a4oRrNty1Rp3ljNhpYZsmGzOyexviNoSQyfLK0jxtE2dhTtE4IiUdZ9En40aeI9V0yccNiAPqSqe7zK0ytW59YteVbHTdzMAolh34w+PLqgoT5WM8AN6ETtds89pqpFXdoxkUw3MoTxP6PY1jZVsj2LxLaZsr5zumzUadJcOVlaR45ny9iRdEyopGuSCGPDS1/6ssMku3yXWSMRGXRv6coubd/veV27YrVmF76oU8ZsY4G4meXj6v4FDfWH+g5RTPmep6gQkZHdc6iIyGhgZOFi7VATPYrKSNq3TpPmjdPZmO1ZJKplA9PcOYkR44OWRCVdk4MiMTO4me1U5bQq0dF5f+OI4YcMdhudFTLi0Xmy/6Pz3OPRW7Vl6VPacHgm1zbvNWaN6GK3vrcQOW/6DlBs+RaVq4DbReS3uCkPzgCuLFiqHfjniK8+PlPWDx9F+/igSIzDDdiK3aCtQvlMc3bkV6ftFNr22kbJhDv3k4Pu3M91iZrcom8ctkafPXRtjtlvMbdCqQ5tZ6XpVd8Bii3vE7UicizwHtyJ0ltV9ZZCButVqup3uJn8TYHkILcoMfuNnEhRftlnv6kvrMjkXj7oKR0xLcsCgapi7LeI/s+Chvq6sDcqIqcDB6jqZ8Pe9lDlfZlWVf8B/KOAWfJhM+kX2DAYdviWtqdWjh1TlKLy8jTZ9ffvqdj19++BYTntmv8ya49cnXtr/+d1woQt7CV+DrPD9IrvAMWW72JirbjDHoARuI5om1W1aFdiAlZUiuCCpubEyrHFv4CTGyYVa+ew19o57rzu8E7duuRZfXzFam1Z8LJOHdXOfMl/aEmpyOvwR0QSwM2qujB4/GVcn6QVwEPAkbjZAj6lqvds99kaXB+yDwA/BFpwaw5NBy5U1etERIDvA8fifpe/rap/EpHLgH+q6l9F5AagSVXPEJFPAbsCv8Y1Ju4FDgm+n+NVtW1H30u+E1+/o1emiJwAHJTPZ0MWu+NTH3br6EyM78qtbq0Ytq/PHB2VMurB+bLowfnu8bg2bT5krTYctibXPncduwzvKouF5V4MYRuVqnqQiBwHfAM4uvsFETkR+CJwnKo2udpBNbAcmI/rrHodcBKwP7AfsBPwbxG5G7gbOCx438zgswSfvya4Pw84VVXPFJFrgQ/hzrP2HnYw36Gq3igiycF8dogaPewzlj7W0pq9fFJpnd7YNFom3rpElt66xDVWpjbra0c8qc8fsjY3bMZG5g3TkpsZsJ1wfma754J+lHcOjzkS1yI5RlVbejx/o6rmgLUisnPw3HLgj6raBbwhInfhlmW9B7hARPYC1gKTxJ1PWwacj+vY+IKqPrGDDO+S7+FPz1nfhgXfiI+uuE/ietXGfhxQoZ2ebdn/8okTtiBSsh3Z3pooM65bLjOuW+6KzNzX9dkjMrlXD3xax0xpZb7kOe6pgJ5d0FCf7yDYTt55aNezr1D3cjhdvPN39nlgLrAH8Egv74e3e6D32hNdVV8NOrO+D9dqmQx8BNikqq0iMmW77XVB3z3B822p9Jz1rRNXfY/P87PhSWW3kap6EljU73vNkIxTHb97R8d9z44YUTYdt56vlt2fr67Y/bfHwLCcdi5s1MyRq3Xjvi/oxHFbWSDufGAxPTWA974BTAt+iTfhZlz8Zz+feRH4MnCDiJysqmv6eO/dwNkiciWucByOWyQQ4AHgAuAoXMvkOoYwB3W+51R8rEa4I49gRaUoPtuUHXPBzqV2RJGf3DCpXD1X9lk91z0e2a6bD3xaVx+R0c17vqrVIzuYV4SR13kXFVXtEJFLcCdlXwAa8vzcUyJyGvBnEeltKZ1uN+AOaVbhjjIuVNV1wWv34A6hnhWRF3FF557eN9O/PvupiMjP6OMwR1XPH+yOBy1VdRZwedH3G0MKuigx+9UukciNSq7arOsPXaNPH7Ym11XAkdefXNBQf0UBtlvS+mupdB+nHQrsBfwpeHwy7oSND772GzsCctSWtmdvGzsmckUlO1Z2+vtBstPfD3KnMbpHXh/coJXTwxt5/XAI2yg7+Q4ovBPXPOoIHg/H9ao9ssD53i1VNQJ3Hb7cO0WVhZcqK1+pmVU9k+BaZSyo6rzXePrI1bl1S54Z9Mjr9Qsa6svz2HGI8i0qTwHLVHVj8HgS8KCq7lngfL1LVf0bdwXKFMFhu8x8ormiYn/fOXwJRl7Xr1itzQtf1MnByOv+Wvk3LmioP7EoAUtMvld/6oDHRGRl8PgIIFWIQHl6BCsqRfOJbOumn02e6DuGN8HI6/0GOPL67qKGLCH5tlQEN5DvAlwxeQKYrqp+jhlTVZ8GfuVl3zHUJrLloDmzuhDx3e+jJAUjr587dG1Oe4y8PmBBQ30sz//l21K5DDeT/ehgjMAk3PrKBxYsWd/u8rTfWBqtOmZBe8e99SNHLPedpRRtnCA737RMdr5pmTvpO+cNXfWD33Q94TeVP/kOzjpYVc8DtgKoahPF70j0tlT2GVzvWlMkn2tqLvbg0bL14s7y9IKG+i7fOXzJt6h0iEgFQZ8VEZmK/zV4Bt3jzwzcYW1b9x2u2ug7R5n4u+8APuVbVH6K65E3TUS+gxsGfWnBUuXnes/7j51jNm8JY8Rt1Cn9d6+PtIHM/Daft2d+u11V6wsZLC+pqgbAz2XtGHqtsuL1986asTMi5TanSTE9nqnNFHVC+FIzkJnfGshzPEIRXQ9c5DtEXMzo7KreqSv36PrKiiW+s5SwG30H8K3c/+LYIVCRnZ5t2db/u2KrC/it7xC+lXdRSWUfw43oNEXy0dbWxahmfecoUf/M1GZe9h3Ct/IuKs5f+n+LCctIZdS+29pX+c5RoqxDJtEoKn/2HSBuzm9qtrWT3+014GbfIUpB+ReVVPYh4N++Y8TJwVu37T0ip8/5zlFifpupzcS2w1tP5V9UnB/4DhA379+8OfbnDnpQ3FIWhugUlb/gJgE2RXJeU3Yv3MzsBm7L1GYafYcoFdEoKqlsF/Bj3zHiZFpX17Sdu7oe852jRNgJ2h6iUVSc3wDrfYeIk083t1hLxc2Cf5PvEKUkOkUllW0Dfu47Rpyc1LppsQSzAcbY9zO1mQ7fIUpJdIqK8/+AHa7xasI1AkYs3rot4zuHRy9if8jeJVpFJZVdj3WTLqoLmpp37v9dkXVxpjZjwxa2E62i4vwYNwbDFMH+29rnj8rlBrISX1SsAq72HaIURa+opLLPAb/0HSNOTti0eV3/74qcZKY243uispIUvaLiXAw0+Q4RF+c0ZRcSrAkVE3dkajOxnoipL9EsKqnsBuAbvmPExZRcbsqMztj0WVHgQt8hSlk0i4rzC2CN7xBxcXZzNi4rGF6bqc3EcumNfEW3qKSyncBnfceIiw9u2rxYVN/ynaPAOoD/8h2i1EW3qACksiuxS8xFUQmVB2/dutZ3jgK7JFObsdHZ/Yh2UXG+DLzpO0QcXLAxO8N3hgK6D/iu7xDlIPpFJZXdCHzBd4w42Lu9fd6YXC6KrZUW4OM2X0p+ol9UAFLZPwB/9R0jDj7cuimKgzo/Z1Mb5C8eRcU5HZtzpeDOam7ZF9UodV2/NlOb+Z3vEOUkPkUllW0CPoQNOCyoqlxu4pzOzqj0WXkFOMd3iHITn6ICkMo+AZzrO0bUndOUHe47QwgUqM3UZqxn9gDFq6gApLJXYGODCurYzVsWDVMt9/FAP8rUZu7wHaIcxa+oOOcDj/gOEVUVULG8bWupLZE7EA9jndwGLZ5FJZXdhju/ssF3lKj6/MbmOb4zDNILwAcytZl230HKVTyLCkAq+xJwKmDD1wtgj46OXcd15cptVrgm4LhMbcY6Sw5BfIsKQCp7G/AV3zGi6tTW1mbfGQagHTgpU5sp58O2khDvogKQyv4Y+JrvGFH0yeaW/VAth0v4CnwyU5tZ6TlHJFhRAUhlvwN803eMqBmvOmG3jrLos3JepjbzB98hosKKSrdUNgV8x3eMqDmvqXm07wz9uChTm/lFWBsTkUtE5OiwtleORFV9Zygtqao64Ku+Y0SFgi5KzH6tS2Sm7yy9+F6mNpMMa2MiUqEFWApWRAT3u1oWFxWspbK9VDaJLaEaGgFZsaXtGd85evHtgRQUEUmISIOIXCkiq0XkOhEZIyKNIvJ1EbkXOFlErhCRDwefaRSRS0XkARF5REQWi8gtIvKciJwTvGeciNwuIo+JSEZEju+xv3oRuQx4DLhYRH7SI8+ZIlKSP6dWVHqTyn4J+KnvGFFxwcbmuZROk7gT+HSmNnPxID67J/BLVd0XNx1C95CPraq6XFWv6eUzL6vqMuAe4Argw8BS4JLuzwInqupi4EjgR0HLpHt/v1PVRcAPgQ+KSPcQiE9SohOQWVHZkVT288BP+n2f6Veis3OXqlxute8cQCtQk6nN/M8gP/+yqt4X3L8KWB7c/1Mfn+meciMDPKSqreqm3dwqIhMBAS4VkdXAv4CZQPcCbS+q6oMAqroZuAN4v4jMB4arakn2A7Ki0pdU9ovAp4EoDeX34uMtra2eI7wKHJapzdw6hG1s39rqfry5j890/+zkeOfPUQ6oBE4DpgJLVHV/3ILvo3aw3V/jpvAo2VYKWFHpXyr7P8AK4HXPScraf2ZbF6G6ydPuM8DSTG1m1RC3s4uILAvunwrcO8TtAVQBb6pqh4gcCexweIOqPgTMBj4G/DGEfReEFZV8pLIPAkuAB31HKVdjVMfu2d7xhIdd3wYsz9RmXglhW/VAbXCoMhm3DMxQXQ0cICKP4Fot/fXovRa4T1VLdkoGu6Q8EKmqEcBlwKd8RylHd40eteqz06ftV8RdXgGclanNDHn1RBFJADer6sKhbmuIOW4GfqKqt/vM0RcrKoORqjoPdxI3CpMRFdWixOwXO0UKPYI5C5wf5jSQvotKcFL3YWCVqp7sI0O+rKgMVqrqcODPwDTfUcrJhVOn3PWPcWOPKOAu/gWckanNvFzAfZg+2DmVwUpl7wYW0vflRLOd85uad6cwPUO34FakPMYKil/WUglDquoE3Em76Z6TlIUjdpn52MaKisUhbvIB3HyypdhzN3aspRKGVPZGYC/ciUHTj9psy9aQNtUOJHH9T6yglAhrqYQtVXUY7gqR16sEpWyrSNuBc2a1I1I1hM08ipsDpSR7lcaZtVTClsreAywCvoTrFm62M0p19ML29sF2268HTgYOtIJSmqylUkipqhm4aRTOBEp9XpGiemDUqCfPqp42kNbcC7iJtK6yNY1LW9kUleA6/cdU9bIBfu4iVb20x+P7VfWQsPP1KVU1DbdI/LnAhKLuu4QtScx+vl1kbj9vew34NvDrMDqxmcIrp6KSYACdj7ontgFaVHXcIPcZ7uQ4qaqJuMueFwBTQtlmGbt4p8krbxw/bsUOXt4A1AE/z9RmymGeWxMop6JyDXA88BRuPMebwEeAkcANqvqNoPD8A7gTWAY8AfwnbkDZGlU9TUQ2qeo4ERkH3ARMwvWM/Zqq3tTLNm4EJqrqF4IcZwILVPWLg/5mUlVjgbOBLwPVg95OmVtXUbHuP2bPmIpIRY+nXwH+G/hppjZj56TKUDkVlQRBS0VEjsFNdnM2rjXyV+D7wEvA88Ah3fNQdBeRHtvpLiqVwBhVbRGRnXCDBefhRon+7zZEZCywGpgfjCS9Hzg7lLksUlUjcUPZz8QNWIydo2bPeOStysrFuEJ+OfB3O2dS3ip9BxikY4Lb48HjcbiC8BI9JrbpR/fkOIfj5rbY4eQ4ItI9OU49YU6O41ZKvBy4nFTVPOCjwW2vULZf+p75XFP26q9PnXKS9YKNjnItKgJ8V1Uvf8eTrjXT14Q5PfWcHKdDRBrpe3Kci3DD0gszOU4q+wzwLeBbpKr2xRWXU4D+TmSWmzeAa4CrSWX/fSJwoudAJlzlVFRagfHB/VuAb4nI1aq6SdxM7Tu6MtAhIsNVdfvXBzQ5jojMBhYD+w7t28hDKrsad8h1Eamqg3EF5sS+MpawNuB+YGVwe4BU1g5vIqxsioqqbhCR+0TkSdzx9x+AB4I5gjcBHwd6+2H9JbBaRB5T1dN6PH818LdgcpwnyG9ynP2LPjlOKvsQ8BDwhaDfy1LcCeSlwAG83boqFW24sTgrg9tDpLK22HmMlM2JWt9KcnKcVNVwYD/eLjJLKe7h0gZcp7TngSexImKwotKvcpocB4BU1TjcYVLP20zc+aOet+4WTg63bEXPW1eP+624wtFdPN6+n8raJV/zLlZU4ipVVUkq2+k7hokeKyrGmFDZKGVjTKisqBhjQmVFxRgTKisqxphQWVExxoTKiooxJlRWVIwxobKiYowJlRUVY0yorKgYY0JlRcUYEyorKsaYUFlRMcaEyoqKMSZUVlSMMaGyomKMCZUVFWNMqKyoGGNCZUXFGBMqKyrGmFBZUTHGhMqKijEmVFZUjDGhsqJijAmVFRVjTKisqBhjQmVFxRgTqv8PAXzustZUhHYAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the pie chart of education categories\n",
    "inp1.education.value_counts(normalize= True).plot.pie()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### poutcome "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#calculate the percentage of each poutcome category.\n",
    "inp1.poutcome.value_counts(normalize= True).plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "inp1[-(inp1.poutcome==\"unknown\")].poutcome.value_counts(normalize= True).plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Response the target variable "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     0.882974\n",
       "yes    0.117026\n",
       "Name: response, dtype: float64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the percentage of each response category.\n",
    "inp1.response.value_counts(normalize= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the pie chart of response categories\n",
    "inp1.response.value_counts(normalize= True).plot.pie()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Session- 4, Bivariate and Multivariate Analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment-2, Numeric- numeric analysis "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There are three ways to analyse the numeric- numeric data types simultaneously.\n",
    "- **Scatter plot**: describes the pattern that how one variable is varying with other variable.\n",
    "- **Correlation matrix**: to describe the linearity of two numeric variables.\n",
    "- **Pair plot**: group of scatter plots of all numeric variables in the data frame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAY4AAAD4CAYAAAD7CAEUAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAfOUlEQVR4nO3df5BdZZ3n8feHTsAGhU4wUEknMUGzscDMGumCIFtToxlMRh3pQSzDmCUzyw5Vrruro5WZZLHKcReKsJkaGWpHZliZEZXlhwEDo2KGIUxtrQXBjkFDgN5EUdKdCFEIshowCd/94z433O7c27nn/r7nfl5VXX3vt8+5/Tz943zv8/MoIjAzM6vWSe0ugJmZdRcnDjMzy8SJw8zMMnHiMDOzTJw4zMwsk2ntLkCjvfnNb44FCxa0uxhmZl1l+/btP4+IWdUcm7vEsWDBAkZGRtpdDDOzriLpp9Ue664qMzPLxInDzMwyceIwM7NMnDjMzCwTJw4zM8skd7OqzMyqsXnHOBu3jLLv4CHmDPSzdsVihpcOtrtYXcGJw8x6zuYd46y/dyeHDh8FYPzgIdbfuxPAyaMK7qoys56zccvosaRRdOjwUTZuGW1TibqLE4eZ9Zx9Bw9littEJ0wckv5e0vOSniiJzZT0oKTd6fOMkq+tl7RH0qikFSXx8yXtTF+7SZJS/BRJd6X4NkkLSs5Zk77HbklrGlZrM+tpcwb6M8VtompaHF8GVk6KrQMeiohFwEPpOZLOBVYB56VzviipL51zM3A1sCh9FF/zKuDFiHgb8AXghvRaM4HPARcCFwCfK01QZma1WrtiMf3T+ybE+qf3sXbF4jaVqLucMHFExP8GXpgUvhS4LT2+DRguid8ZEa9GxDPAHuACSbOB0yPikSjcq/Yrk84pvtYmYHlqjawAHoyIFyLiReBBjk9gZmaZDS8d5PrLljA40I+AwYF+rr9siQfGq1TrGMfZEbEfIH0+K8UHgb0lx42l2GB6PDk+4ZyIOAK8BJw5xWsdR9LVkkYkjRw4cKDGKpmZWTUaPTiuMrGYIl7rORODEbdExFBEDM2aVdWuwGbWw4rTcccPHiJ4fTru5h3j7S5aV6g1cTyXup9In59P8TFgXslxc4F9KT63THzCOZKmAWdQ6Bqr9FpmZnXxdNz61Jo47geKs5zWAPeVxFelmVILKQyCP5a6s16WtCyNX1w56Zzia10ObE3jIFuA90makQbF35diZmZ18XTc+pxw5bikO4DfAd4saYzCTKcNwN2SrgKeBT4CEBG7JN0NPAkcAT4REcW0/nEKM7T6gQfSB8CtwFcl7aHQ0liVXusFSf8N+F467r9GxORBejOzzOYM9DNeJkl4Om51VHhznx9DQ0PhOwCa2VQmbzkChem4vTyzStL2iBiq5ljvVWVmPaeYHLzJYW2cOMysJw0vHXSiqJH3qjIzs0ycOMzMLBMnDjMzy8SJw8zMMnHiMDOzTJw4zMwsEycOMzPLxInDzMwyceIwM7NMnDjMzCwTJw4zM8vEicPMzDJx4jAzs0ycOMzMLBMnDjMzy8SJw8zMMnHiMDOzTJw4zMwsEycOMzPLxInDzMwyceIwM7NMnDjMzCwTJw4zM8tkWrsLYNZtPrt5J3ds28vRCPokrrhwHtcOL2l3scxaxonDLIPPbt7J1x599tjzoxHHnjt5WK+oq6tK0p9K2iXpCUl3SHqDpJmSHpS0O32eUXL8ekl7JI1KWlESP1/SzvS1myQpxU+RdFeKb5O0oJ7ymtXrjm17M8XN8qjmxCFpEPjPwFBEvAPoA1YB64CHImIR8FB6jqRz09fPA1YCX5TUl17uZuBqYFH6WJniVwEvRsTbgC8AN9RaXrNGOBqRKW6WR/UOjk8D+iVNA04F9gGXArelr98GDKfHlwJ3RsSrEfEMsAe4QNJs4PSIeCQiAvjKpHOKr7UJWF5sjZi1Q1+FP79KcbM8qjlxRMQ48JfAs8B+4KWI+Cfg7IjYn47ZD5yVThkEStvzYyk2mB5Pjk84JyKOAC8BZ04ui6SrJY1IGjlw4ECtVTI7oSsunJcpbpZH9XRVzaDQIlgIzAFOk7R6qlPKxGKK+FTnTAxE3BIRQxExNGvWrKkLblaHa4eXsHrZ/GMtjD6J1cvme2Dceko9s6p+F3gmIg4ASLoXeDfwnKTZEbE/dUM9n44fA0rfls2l0LU1lh5PjpeeM5a6w84AXqijzGZ1u3Z4iROF9bR6xjieBZZJOjWNOywHngLuB9akY9YA96XH9wOr0kyphRQGwR9L3VkvS1qWXufKSecUX+tyYGsaBzEzszapucUREdskbQK+DxwBdgC3AG8E7pZ0FYXk8pF0/C5JdwNPpuM/ERFH08t9HPgy0A88kD4AbgW+KmkPhZbGqlrLa2ZmjaG8vYEfGhqKkZGRdhfDzKyrSNoeEUPVHOu9qszMLBMnDjMzy8SJw8zMMnHiMDOzTJw4zMwsEycOMzPLxInDzMwy8Y2czDLavGOcjVtG2XfwEHMG+lm7YjHDSwdPfKJZTjhxmGWwecc46+/dyaHDhU0Pxg8eYv29OwGcPKxnuKvKLIONW0aPJY2iQ4ePsnHLaJtKZNZ6ThxmGew7eChT3CyPnDjMMpgz0J8pbpZHThxmGaxdsZj+6X0TYv3T+1i7YnGbSmTWeh4cN8ugOADuWVXWy5w4zDIaXjroRGE9zYkjZ7zGwKw6/l+pnRNHjniNgVl1/L9SHw+O54jXGJhVx/8r9XHiyBGvMTCrjv9X6uOuqhyZM9DPeJk/fK8xqMz93L3J/yv1cYsjR7zGIJtiP/f4wUMEr/dzb94x3u6iWZP5f6U+Thw5Mrx0kOsvW8LgQD8CBgf6uf6yJX4HXYH7uXuX/1fq466qnPEag+q5n7u3+X+ldm5xWM/yvlNmtXHisJ7lfm6z2rirynqW950yq40Th/U093ObZVdXV5WkAUmbJD0t6SlJF0maKelBSbvT5xklx6+XtEfSqKQVJfHzJe1MX7tJklL8FEl3pfg2SQvqKa+ZWR5t3jHOxRu2snDdt7h4w9amTymvd4zjr4HvRMTbgX8NPAWsAx6KiEXAQ+k5ks4FVgHnASuBL0oqdjDfDFwNLEofK1P8KuDFiHgb8AXghjrLa2aWK+1Yj1Rz4pB0OvDbwK0AEfGbiDgIXArclg67DRhOjy8F7oyIVyPiGWAPcIGk2cDpEfFIRATwlUnnFF9rE7C82Bqx8lr9zqPb+edl3a4d65HqaXGcAxwA/kHSDklfknQacHZE7AdIn89Kxw8Ce0vOH0uxwfR4cnzCORFxBHgJOHNyQSRdLWlE0siBAwfqqFJ380robPzzsjxox3qkehLHNOBdwM0RsRT4FalbqoJyLYWYIj7VORMDEbdExFBEDM2aNWvqUueYV0Jnk7efl1tPvakd65HqSRxjwFhEbEvPN1FIJM+l7ifS5+dLjp9Xcv5cYF+Kzy0Tn3COpGnAGcALdZQ517wSOps8/bzceupd7ViPVHPiiIifAXslFUu3HHgSuB9Yk2JrgPvS4/uBVWmm1EIKg+CPpe6slyUtS+MXV046p/halwNb0ziIleGV0Nnk6eeVt9aTVa8d+27Vu47jPwG3SzoZ+DHwxxSS0d2SrgKeBT4CEBG7JN1NIbkcAT4REcW/9I8DXwb6gQfSBxQG3r8qaQ+FlsaqOsuba2tXLJ5wVzPwSuipvOfts/jao8+WjXebPLWeLLtWr0eqK3FExOPAUJkvLa9w/HXAdWXiI8A7ysRfISUeOzGvhM7m4afLT6SoFO9kvr+EtZJXjueMV0JXL0/v0t3atFbyJofWs/I0xuH7S1grucVhPStv79Ld2rRWceKwnuUxIbPaOHFYT2vVu/TPbt7JHdv2cjSCPokrLpzHtcNLmv59rbLNO8Zz86ah1XVx4jBrss9u3jlh2u/RiGPPnTzao7hgsthNWVwwCXRd8mhHXTw4btZkd2zbmyluzZenBZPdtsmhmVXhaIXNDirFrfnyNBW73PqdqeKN4MRh1mR9Fe4EUCluzZenqdjt+Pty4jBrsisunJcpbs3Xjo0Bm6UdLVoPjps1WXEA3LOqOkeepmIPVthuZrCJrSflbbPZoaGhGBkZaXcxzMxaYvKsKii0nrLuHCBpe0SU23vwOG5xmJl1sXa0npw4zMy6XKu3m/HguJmZZeLEYWZmmbirynpanvYrMmsVJw7rWa3c48cJyvLEiaNL+MLTeFPt8dPIn22eNtQzAyeOpmnkhd4XnuZo1X5FrUpQlo3fjNXOg+NNULzQjx88RPD6hX7zjvGaXi9PO3l2klbtV5SnDfXyotH/o73GiaMJGn2h94WnOVq1X1GeNtTLC78Zq48TRxM0+kLvC09zDC8d5PrLljA40I8o7O2TdZuGauRpQ728aMdW5HniMY4mmFNh07FaL/RrVywuuxeNLzz1a8WK2zxtqJcXfVLZ3WO7dav7Vt+a2ImjCRp9ofeFp/u1eksIm1qebq7VjlsTO3E0QTMu9L7wdA7Pxul+M06dzou/Plw23m2mujWxE0eX8YU+nzw1Oh8qNSy6sMHRltZT3YPjkvok7ZD0zfR8pqQHJe1On2eUHLte0h5Jo5JWlMTPl7Qzfe0mqdDRKOkUSXel+DZJC+otr1k9PBsnH146dHxrY6p4J+vWW8d+Eniq5Pk64KGIWAQ8lJ4j6VxgFXAesBL4oqTiVJObgauBReljZYpfBbwYEW8DvgDc0IDytsTmHeNcvGErC9d9i4s3bPX88Jzw1Oh8yNNMxXbcmriuxCFpLvAB4Esl4UuB29Lj24DhkvidEfFqRDwD7AEukDQbOD0iHonC7Qi/Mumc4mttApYXWyOdzIuL8itPF5xe9p63z8oU72TXDi9h9bL5x1oYfRKrl83v6FlVNwJ/BrypJHZ2ROwHiIj9ks5K8UHg0ZLjxlLscHo8OV48Z296rSOSXgLOBH5eWghJV1NosTB//vw6q1Q/bzGRX54anQ8PP30gU7zTXTu8pKX3sK+5xSHpg8DzEbG92lPKxGKK+FTnTAxE3BIRQxExNGtW+98xuDsjv1q1aNCaywsA61NPi+Ni4EOS3g+8AThd0teA5yTNTq2N2cDz6fgxoLTTbS6wL8XnlomXnjMmaRpwBvBCHWVuiUYvADQzm0qrp4jX3OKIiPURMTciFlAY9N4aEauB+4E16bA1wH3p8f3AqjRTaiGFQfDHUrfWy5KWpfGLKyedU3yty9P36PgJc95iIr88fmWdph1/k83Yq2oDcImk3cAl6TkRsQu4G3gS+A7wiYgodhR/nMIA+x7gR8ADKX4rcKakPcCnSTO0Ot3w0kE+fP7ghMGqD5/vdR154Om41mna8TfZkAWAEfEvwL+kx78Allc47jrgujLxEeAdZeKvAB9pRBlbafOOce7ZPn5sAc7RCO7ZPs7QW2Y6eXS5WsevWr2XkPWOdoypenfcJvC70vyqZTpucS+h0jcSX3v0WT67eWdTymi9pR1TxJ04msCzqvKrlvGr27c9myluzXdShdVgleKdrB1jqk4cTeBFYvlVy3TcPO2LlBcXnTMzU7yTtWOKuDc5bAIvEsu3kZ++wM9eeoUAfvbSK4z89AWPXXWZn/yifOu/UrzTtXpTVSeOJvD9M/KrHfc+sMZzd3J9nDiaxNuq59Ptj1YYr3j02YqJI0/3fsiLgQq/kwH/TqriMQ6zDCoNS0w1XPGB35qdKW7N53Gn+jhxmDXZPdvHMsWt+Q5WuO9GpbhN5MRhlsFpJ/dligMcOvxaprg1XztufpQnThxmGVz3B0uO27JZKW7dox23W80TD47njLe26DwnCV4rcz1q9GKzVu+Q2s3yNmGha3bHtc7jrS2a77/c+8PjBsIjxSt566zTMsVr4V17s/l/r5Qfy6gU72R52R3X2uSObXszxS27X1cYl6gUB/jxgV9nitfC+6NlU+nX1Y3DTu343Ttx5Ij7bTtTK34vXtDWu9rxu/cYR5eopg+zTyp7MfJMkcaRys/1b/eP2Hed7F1n9E8vO434jP7mjde4xdEFqu3DvOLCeWXPrxS3ws/24g1bWbjuW1y8YesJ+4U/duH8TPFWWbtiMdMnjbZPP0neH60HVHrT0sw3M04cXaDaPsxrh5ewetn8CXceXL1svmdVVbB5xzhrN/1gQkJeu+kHUyaPobeU3z21Urylys0Tttw7WGZ22FTxRnBXVRco1wVRKX7t8BIniip9/h93cfjoxH6nw0eDz//jropTGa/5RvkZatd8Y2dbp75u3DJati4bt4x6Sm7OtaOb0i2OLuBVrs1Rbh7/VHGAX/3maKZ4q3hwvHe95+2zMsUbwS2OjNqxyCrLrBwvAus8q5fNn7AVe2m8UTw43rsefvpApngjuMWRweYd43zm6xP7xD/z9fJ94lkHXacyWOGff3Lci8CyqdRem6odV8s5reDB8d7VjtamE0cG13xjJ0cn7R1x9LU4rt+70RfwBWeWTxyT414Elk0tW6S/+63lB8ErxYGyrY2p4jXz4HhPasetqp04Mqi2f7vRF/BHf/xiVfEsg+hWfUuu1K59L2eKt8pUg+OWb+0Y43DiaIJGNx2rHeNox3zublapG2eq7p1OvY+DB8d717d+uD9TvBGcODKotn+70U3HamdV+a5m2fzNw7szxTtZpVue+lao+VfL7MB6OXFk8LEKs2Amx9euWEz/9Ik39umf3lfzQOWyc2Zkilt1dj//q0xx6NzBcb9psFaqOXFImifpYUlPSdol6ZMpPlPSg5J2p88zSs5ZL2mPpFFJK0ri50vamb52k1R4Ky3pFEl3pfg2SQvqqGvdql2ZPbx0kOsvW8LgQD+i0Gd+/WVLap4W+5NflO9uqBS35qllQL0VOrULzZpvoMKeVJXijVDPOo4jwGci4vuS3gRsl/Qg8EfAQxGxQdI6YB3w55LOBVYB5wFzgH+W9K8i4ihwM3A18CjwbWAl8ABwFfBiRLxN0irgBuCjdZS5omrXP7RjZbYHve1EWnWzKOs8r71Wfi/4SvFGqLnFERH7I+L76fHLwFPAIHApcFs67DZgOD2+FLgzIl6NiGeAPcAFkmYDp0fEIxERwFcmnVN8rU3A8mJrpJFq2bOola/nlePdrZb7lGdVLmlMFbf8+OWr5Wd7Voo3QkPGOFIX0lJgG3B2ROyHQnIBzkqHDQKldxQaS7HB9HhyfMI5EXEEeAk4sxFlLjXVnkWd8HrVzqqaVuHtZaV4r2vFBR06d5sSs1rVnTgkvRG4B/hURPxyqkPLxGKK+FTnTC7D1ZJGJI0cOJB9mX2jZyU0+vWqXW9wpMLby0rxXucLullt6kockqZTSBq3R8S9Kfxc6n4ifX4+xceA0htDzAX2pfjcMvEJ50iaBpwBvDC5HBFxS0QMRcTQrFnNW/TSLo2epWVmVo96ZlUJuBV4KiL+quRL9wNr0uM1wH0l8VVpptRCYBHwWOrOelnSsvSaV046p/halwNb0zhITxleOsiHzx+cMJvrw+cPevNCO8bjYNZK9bQ4Lgb+LfBeSY+nj/cDG4BLJO0GLknPiYhdwN3Ak8B3gE+kGVUAHwe+RGHA/EcUZlRBITGdKWkP8GkKM7QartNXXG/eMc5d39t7bEzjaAR3fW+vNy+0Y3z3x97VjrVFNU/HjYj/Q+WyLa9wznXAdWXiI8A7ysRfAT5SaxmrlWXxVDu2La/lhkPWW4pTxO/YVniD0SdxxYXzfFOvHtCOtUW+HweFQeZyayIqbVte3MCwuOst0NQLeDu2FLDu47s/Wqt4yxGq313S25ZbJ2vkPWDMpuIWB9XfQavaFdxS+W6uThkzsfwpLjotdmkWF51Cc1vD1pvc4qD6Lam9S611qkYvOjWbihMH1W+DnuXe32at5HEwayUnDtpzBy0zs0aodBFv5sXdiYPqxzjMzDpNpT1wm7c3rhMH4Ntumpll4cQBnFHhhieT45169zczs1Zy4qD6LUecOMzMnDgAOFhh5snkeDv6Es3MOo0TB9VPxzUzMycOwNNxzcyycOIA7tk+liluZtbLnDiAQ4fLj1JUipuZ9TInDjMzy8SJw8zMMnHiMDOzTJw4zMwsEycOMzPLxInDzMwyceIwM7NMnDjMzCwTJw4zM8vEicPMzDJx4jAzs0ycOMzMLJOuSBySVkoalbRH0rp2l8fMrJd1fOKQ1Af8DfB7wLnAFZLObW+pzMx6V8cnDuACYE9E/DgifgPcCVza5jKZmfWsbkgcg8DekudjKWZmZm3QDYlDZWIx4QDpakkjkkYOHDjQomKZmfWmbkgcY8C8kudzgX2lB0TELRExFBFDs2b5PuFmZs3UDYnje8AiSQslnQysAu5vc5nMzHpWxyeOiDgC/EdgC/AUcHdE7Grk9/jJhg9UFb/xo+8se1yluJlZHk1rdwGqERHfBr7dzO9RKXmUGl5aGJPfuGWUfQcPMWegn7UrFh+LF9340XfyqbseP+78WhPMQP90Dh46XDZurXX2m07muZd/UzZu1g4nCV6L8vGmfc/mvXQ+DS8d5Lvr3sszGz7Ad9e997ikUTzmxo++k8GBfgQMDvRz40ffWfbYavzFh85j+qS/guknib/40HkTYqdMK//rrBTvddW2NEttu+aS45LE2W86mW3XXNLQsmW1etn8THHLjz+8sPzvuFK8EbqixdGNhpcO1pwoyr0WnLilc8OHf4tP3/34hHcfJ6kQt/KqaWlO1u4kUc61w0sAuGPbXo5G0CdxxYXzjsUtv9rxu1dEmTZOFxsaGoqRkZF2F6NtNu8YP2GCsdb62P98hO/+6IXj4he/dSa3/8lFbSiRLVj3rYpfq+XNRB5I2h4RQ9Uc6xZHzjSypWONcfufXHRc8nDSaK8Zp07nxV8fP24441SPG1bDicOsBZwkOsvnfv88PvP1H3C0pF+37yTxud8/b4qzrMijpmbWkyZf/HwxrJ5bHDnjMQ6zE9u4ZZTDk+awHn4t2Lhl1P8vVXDiyJHNO8ZZf+9ODh0+CsD4wUOsv3cngP8ZzErsO3goU9wmcussRzZuGT2WNIoOHT7Kxi2jbSqRWWeaM9CfKW4TOXHkiN9FmVVn7YrF9E/vmxDrn97H2hWL21Si7uLEkSN+F2VWneGlg1x/2ZIJuztcf9kSd+lWyWMcObJ2xeIJYxzgd1FmlXjNU+2cOHKk2q1JzMzq4cSRM34XZWbN5jEOMzPLxInDzMwyceIwM7NMnDjMzCwTJw4zM8skdzdyknQA+GkdL/Fm4OcNKk475aUe4Lp0qrzUJS/1gPrq8paImFXNgblLHPWSNFLtXbA6WV7qAa5Lp8pLXfJSD2hdXdxVZWZmmThxmJlZJk4cx7ul3QVokLzUA1yXTpWXuuSlHtCiuniMw8zMMnGLw8zMMnHiMDOzTJw4EkkrJY1K2iNpXbvLAyBpnqSHJT0laZekT6b4TEkPStqdPs8oOWd9qsOopBUl8fMl7Uxfu0mSUvwUSXel+DZJC5pcpz5JOyR9s5vrImlA0iZJT6ffz0XdWBdJf5r+tp6QdIekN3RLPST9vaTnJT1REmtJ2SWtSd9jt6Q1TarLxvT39UNJ35A00DF1iYie/wD6gB8B5wAnAz8Azu2Acs0G3pUevwn4v8C5wH8H1qX4OuCG9PjcVPZTgIWpTn3pa48BFwECHgB+L8X/A/C36fEq4K4m1+nTwP8Cvpmed2VdgNuAf58enwwMdFtdgEHgGaA/Pb8b+KNuqQfw28C7gCdKYk0vOzAT+HH6PCM9ntGEurwPmJYe39BJdWnZRbCTP9IPekvJ8/XA+naXq0w57wMuAUaB2Sk2GxgtV25gS6rbbODpkvgVwN+VHpMeT6Ow6lRNKv9c4CHgvbyeOLquLsDpFC64mhTvqrpQSBx700VjGvDNdLHqmnoAC5h4sW162UuPSV/7O+CKRtdl0tf+ALi9U+rirqqC4j9Q0ViKdYzUtFwKbAPOjoj9AOnzWemwSvUYTI8nxyecExFHgJeAM5tSCbgR+DPgtZJYN9blHOAA8A+p2+1Lkk7rtrpExDjwl8CzwH7gpYj4p26rxyStKHs7rhf/jkILYkK5Jn3/ltXFiaNAZWIdM09Z0huBe4BPRcQvpzq0TCymiE91TkNJ+iDwfERsr/aUMrGOqAuFd2zvAm6OiKXAryh0i1TSkXVJ/f+XUujumAOcJmn1VKdUKFMn/E5OpJFlb2mdJF0DHAFur6NcDa2LE0fBGDCv5PlcYF+byjKBpOkUksbtEXFvCj8naXb6+mzg+RSvVI+x9HhyfMI5kqYBZwAvNL4mXAx8SNJPgDuB90r6WpfWZQwYi4ht6fkmComk2+ryu8AzEXEgIg4D9wLv7sJ6lGpF2Vt2vUiD1R8EPhapL2mK79+yujhxFHwPWCRpoaSTKQwe3d/mMpFmRNwKPBURf1XypfuB4uyHNRTGPorxVWkGxUJgEfBYarK/LGlZes0rJ51TfK3Lga0lf6ANExHrI2JuRCyg8PPdGhGru7QuPwP2SlqcQsuBJ7uwLs8CyySdmr7/cuCpLqxHqVaUfQvwPkkzUqvtfSnWUJJWAn8OfCgifj2pju2tS6MGqbr9A3g/hVlLPwKuaXd5Upn+DYVm4w+Bx9PH+yn0TT4E7E6fZ5acc02qwyhpRkWKDwFPpK/9D17fNeANwNeBPRRmZJzTgnr9Dq8PjndlXYB3AiPpd7OZwoyUrqsL8Hng6VSGr1KYqdMV9QDuoDA2c5jCO+erWlV2CmMOe9LHHzepLnsojD88nj7+tlPq4i1HzMwsE3dVmZlZJk4cZmaWiROHmZll4sRhZmaZOHGYmVkmThxmZpaJE4eZmWXy/wFMwvAM2m12owAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the scatter plot of balance and salary variable in inp1\n",
    "plt.scatter(inp1.salary, inp1.balance)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the scatter plot of balance and age variable in inp1\n",
    "inp1.plot.scatter(x='age', y='balance')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 540x540 with 12 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the pair plot of salary, balance and age in inp1 dataframe.\n",
    "sns.pairplot(data=inp1, vars=[\"salary\",\"balance\", \"age\"])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Correlation heat map "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the correlation matrix of salary, balance and age in inp1 dataframe.\n",
    "sns.heatmap( inp1[[\"salary\",\"balance\", \"age\"]].corr(), annot= True, cmap= \"Reds\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 4, Numerical categorical variable"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Salary vs response "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "response\n",
       "no     56769.510482\n",
       "yes    58780.510880\n",
       "Name: salary, dtype: float64"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#groupby the response to find the mean of the salary with response no & yes seperatly.\n",
    "inp1.groupby(\"response\")[\"salary\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "response\n",
       "no     60000.0\n",
       "yes    60000.0\n",
       "Name: salary, dtype: float64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#groupby the response to find the median of the salary with response no & yes seperatly.\n",
    "inp1.groupby(\"response\")[\"salary\"].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the box plot of salary for yes & no responses.\n",
    "sns.boxplot(data=inp1,x=\"response\", y=\"salary\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Balance vs response "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the box plot of balance for yes & no responses.\n",
    "sns.boxplot(data=inp1,x=\"response\", y=\"balance\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "response\n",
       "no     1304.292281\n",
       "yes    1804.681362\n",
       "Name: balance, dtype: float64"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#groupby the response to find the mean of the balance with response no & yes seperatly.\n",
    "inp1.groupby(\"response\")[\"balance\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "response\n",
       "no     417.0\n",
       "yes    733.0\n",
       "Name: balance, dtype: float64"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#groupby the response to find the median of the balance with response no & yes seperatly.\n",
    "inp1.groupby(\"response\")[\"balance\"].median()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### 75th percentile "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "#function to find the 75th percentile.\n",
    "def p75(x):\n",
    "    return np.quantile(x, 0.75)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=0c0bddcd-c9d2-4ad9-b185-36a27608a8e5 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('0c0bddcd-c9d2-4ad9-b185-36a27608a8e5').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>mean</th>\n",
       "      <th>median</th>\n",
       "      <th>p75</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>response</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>no</th>\n",
       "      <td>1304.292281</td>\n",
       "      <td>417.0</td>\n",
       "      <td>1345.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>yes</th>\n",
       "      <td>1804.681362</td>\n",
       "      <td>733.0</td>\n",
       "      <td>2159.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "                 mean  median     p75\n",
       "response                             \n",
       "no        1304.292281   417.0  1345.0\n",
       "yes       1804.681362   733.0  2159.0"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the mean, median and 75th percentile of balance with response\n",
    "inp1.groupby(\"response\")[\"balance\"].aggregate([\"mean\",\"median\",p75])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the bar graph of balance's mean an median with response.\n",
    "inp1.groupby(\"response\")[\"balance\"].aggregate([\"mean\",\"median\"]).plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Education vs salary "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "education\n",
       "primary      34232.343910\n",
       "secondary    49731.449525\n",
       "tertiary     82880.249887\n",
       "unknown      46529.633621\n",
       "Name: salary, dtype: float64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#groupby the education to find the mean of the salary education category.\n",
    "inp1.groupby(\"education\")[\"salary\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "education\n",
       "primary       20000.0\n",
       "secondary     55000.0\n",
       "tertiary     100000.0\n",
       "unknown       50000.0\n",
       "Name: salary, dtype: float64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#groupby the education to find the median of the salary for each education category.\n",
    "inp1.groupby(\"education\")[\"salary\"].median()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Job vs salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "job\n",
       "admin.            50000.0\n",
       "blue-collar       20000.0\n",
       "entrepreneur     120000.0\n",
       "housemaid         16000.0\n",
       "management       100000.0\n",
       "retired           55000.0\n",
       "self-employed     60000.0\n",
       "services          70000.0\n",
       "student            4000.0\n",
       "technician        60000.0\n",
       "unemployed         8000.0\n",
       "unknown               0.0\n",
       "Name: salary, dtype: float64"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#groupby the job to find the mean of the salary for each job category.\n",
    "inp1.groupby('job')['salary'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "job\n",
       "admin.            50000.0\n",
       "blue-collar       20000.0\n",
       "entrepreneur     120000.0\n",
       "housemaid         16000.0\n",
       "management       100000.0\n",
       "retired           55000.0\n",
       "self-employed     60000.0\n",
       "services          70000.0\n",
       "student            4000.0\n",
       "technician        60000.0\n",
       "unemployed         8000.0\n",
       "unknown               0.0\n",
       "Name: salary, dtype: float64"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1.groupby('job')['salary'].median()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment- 5, Categorical categorical variable "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     39876\n",
       "yes     5285\n",
       "Name: response, dtype: int64"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create response_flag of numerical data type where response \"yes\"= 1, \"no\"= 0\n",
    "inp1[\"response_flag\"]=np.where(inp1.response==\"yes\", 1, 0)\n",
    "inp1.response.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     0.882974\n",
       "yes    0.117026\n",
       "Name: response, dtype: float64"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1.response.value_counts(normalize= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.1170257523084077"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1.response_flag.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Education vs response rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "education\n",
       "primary      0.086416\n",
       "secondary    0.105608\n",
       "tertiary     0.150083\n",
       "unknown      0.135776\n",
       "Name: response_flag, dtype: float64"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the mean of response_flag with different education categories.\n",
    "inp1.groupby(\"education\")[\"response_flag\"].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Marital vs response rate "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "marital\n",
       "divorced    0.119469\n",
       "married     0.101269\n",
       "single      0.149554\n",
       "Name: response_flag, dtype: float64"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#calculate the mean of response_flag with different marital status categories.\n",
    "inp1.groupby([\"marital\"])[\"response_flag\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the bar graph of marital status with average value of response_flag\n",
    "inp1.groupby([\"marital\"])[\"response_flag\"].mean().plot.barh()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Loans vs response rate "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the bar graph of personal loan status with average value of response_flag\n",
    "inp1.groupby([\"loan\"])[\"response_flag\"].mean().plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Housing loans vs response rate "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXoAAAEOCAYAAACHE9xHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAATNklEQVR4nO3df6xfd33f8eer13g00GCkXI3MtmoHWWTu2pHsykobhiZYNztBmG3d6kgQlkm1rMVNMhW1LtoWbX91FWtLJCuumxg1IqtVpWy16BWmE80k1CT45odCjbG4M+l8caJcREmgQXHcvPfH90T96uZrf8+17/UXPn4+pK98zufX9/2Nbl4+Pvd8z0lVIUlq149NugBJ0uoy6CWpcQa9JDXOoJekxhn0ktQ4g16SGrdm0gWMcs0119SmTZsmXYYk/ch48sknv11V06P6fiiDftOmTczNzU26DEn6kZHkL8/X56kbSWqcQS9JjTPoJalxBr0kNc6gl6TGGfSS1DiDXpIaZ9BLUuN+KL8w9aNg074/mXQJTXnuN26ddAlSszyil6TGGfSS1DiDXpIaZ9BLUuN6BX2S7UlOJplPsm9E//VJHkvyapJPLOlbl+SRJF9PciLJz65U8ZKk8cZedZNkCtgP/DywABxLcqSqvjY07DvAXcBHRizxaeALVfULSdYCV11y1ZKk3voc0W8D5qvqVFWdBQ4DO4cHVNWLVXUMeG24PcnVwPuBB7txZ6vquytRuCSpnz5Bvx44PbS/0LX1cR2wCHwmydNJHkjytmXWKEm6BH2CPiPaquf6a4Abgfur6gbgr4E3neMHSLI7yVySucXFxZ7LS5LG6RP0C8DGof0NwJme6y8AC1X1RLf/CIPgf5OqOlhVM1U1Mz098rGHkqSL0CfojwFbkmzufpm6CzjSZ/GqegE4neQ9XdMHga9dYIokaYWNveqmqs4l2QscBaaAQ1V1PMmerv9AkncBc8DVwOtJ7gG2VtXLwC8DD3d/SZwC7lidjyJJGqXXTc2qahaYXdJ2YGj7BQandEbNfQaYufgSJUmXwm/GSlLjDHpJapxBL0mNM+glqXEGvSQ1zqCXpMYZ9JLUOINekhpn0EtS4wx6SWqcQS9JjTPoJalxBr0kNc6gl6TGGfSS1DiDXpIa1yvok2xPcjLJfJI3Pdw7yfVJHkvyapJPjOifSvJ0ks+vRNGSpP7GBn2SKWA/sAPYCtyWZOuSYd8B7gI+dZ5l7gZOXEKdkqSL1OeIfhswX1WnquoscBjYOTygql6sqmPAa0snJ9kA3Ao8sAL1SpKWqU/QrwdOD+0vdG19/Q7wq8Dry5gjSVohfYI+I9qqz+JJPgS8WFVP9hi7O8lckrnFxcU+y0uSeugT9AvAxqH9DcCZnuvfDHw4yXMMTvl8IMlnRw2sqoNVNVNVM9PT0z2XlySN0yfojwFbkmxOshbYBRzps3hV/XpVbaiqTd28L1XVRy+6WknSsq0ZN6CqziXZCxwFpoBDVXU8yZ6u/0CSdwFzwNXA60nuAbZW1curV7okqY+xQQ9QVbPA7JK2A0PbLzA4pXOhNR4FHl12hZKkS+I3YyWpcQa9JDXOoJekxhn0ktQ4g16SGmfQS1LjDHpJapxBL0mNM+glqXEGvSQ1zqCXpMYZ9JLUOINekhpn0EtS4wx6SWqcQS9JjesV9Em2JzmZZD7JvhH91yd5LMmrST4x1L4xyZ8lOZHkeJK7V7J4SdJ4Y58wlWQK2A/8PIMHhR9LcqSqvjY07DvAXcBHlkw/B/xKVT2V5CeAJ5P86ZK5kqRV1OeIfhswX1WnquoscBjYOTygql6sqmPAa0van6+qp7rt7wEngPUrUrkkqZc+Qb8eOD20v8BFhHWSTcANwBPLnStJunh9gj4j2mo5b5Lk7cAfAfdU1cvnGbM7yVySucXFxeUsL0m6gD5BvwBsHNrfAJzp+wZJ3sIg5B+uqs+db1xVHayqmaqamZ6e7ru8JGmMPkF/DNiSZHOStcAu4EifxZMEeBA4UVW/dfFlSpIu1tirbqrqXJK9wFFgCjhUVceT7On6DyR5FzAHXA28nuQeYCvwM8DHgK8meaZb8pNVNbvin0SSNNLYoAfognl2SduBoe0XGJzSWerLjD7HL0m6TPxmrCQ1zqCXpMYZ9JLUOINekhpn0EtS4wx6SWqcQS9JjTPoJalxBr0kNc6gl6TGGfSS1DiDXpIaZ9BLUuMMeklqnEEvSY0z6CWpcb2CPsn2JCeTzCfZN6L/+iSPJXk1ySeWM1eStLrGBn2SKWA/sIPB4wFvS7J1ybDvAHcBn7qIuZKkVdTniH4bMF9Vp6rqLHAY2Dk8oKperKpjwGvLnStJWl19gn49cHpof6Fr6+NS5kqSVkCfoB/1cO/quX7vuUl2J5lLMre4uNhzeUnSOH2CfgHYOLS/ATjTc/3ec6vqYFXNVNXM9PR0z+UlSeP0CfpjwJYkm5OsBXYBR3qufylzJUkrYM24AVV1Lsle4CgwBRyqquNJ9nT9B5K8C5gDrgZeT3IPsLWqXh41d5U+iyRphLFBD1BVs8DskrYDQ9svMDgt02uuJOny8ZuxktQ4g16SGmfQS1LjDHpJapxBL0mNM+glqXEGvSQ1zqCXpMYZ9JLUOINekhpn0EtS4wx6SWqcQS9JjTPoJalxBr0kNa5X0CfZnuRkkvkk+0b0J8l9Xf+zSW4c6vsPSY4n+Yskf5DkrSv5ASRJFzY26JNMAfuBHcBW4LYkW5cM2wFs6V67gfu7ueuBu4CZqvoHDJ4ytWvFqpckjdXniH4bMF9Vp6rqLHAY2LlkzE7goRp4HFiX5Nqubw3w40nWAFfR/8HikqQV0Cfo1wOnh/YXuraxY6rqW8CngP8HPA+8VFVfvPhyJUnL1SfoM6Kt+oxJ8k4GR/ubgb8HvC3JR0e+SbI7yVySucXFxR5lSZL66BP0C8DGof0NvPn0y/nG/FPgm1W1WFWvAZ8Dfm7Um1TVwaqaqaqZ6enpvvVLksboE/THgC1JNidZy+CXqUeWjDkC3N5dfXMTg1M0zzM4ZXNTkquSBPggcGIF65ckjbFm3ICqOpdkL3CUwVUzh6rqeJI9Xf8BYBa4BZgHXgHu6PqeSPII8BRwDngaOLgaH0SSNNrYoAeoqlkGYT7cdmBou4A7zzP3XuDeS6hR0jJt2vcnky6hKc/9xq2TLuGS+M1YSWqcQS9JjTPoJalxBr0kNc6gl6TGGfSS1DiDXpIaZ9BLUuMMeklqnEEvSY0z6CWpcQa9JDXOoJekxhn0ktQ4g16SGmfQS1LjegV9ku1JTiaZT7JvRH+S3Nf1P5vkxqG+dUkeSfL1JCeS/OxKfgBJ0oWNDfokU8B+YAewFbgtydYlw3YAW7rXbuD+ob5PA1+oquuBf4jPjJWky6rPEf02YL6qTlXVWeAwsHPJmJ3AQzXwOLAuybVJrgbeDzwIUFVnq+q7K1e+JGmcPkG/Hjg9tL/QtfUZcx2wCHwmydNJHkjytkuoV5K0TH2CPiPaqueYNcCNwP1VdQPw18CbzvEDJNmdZC7J3OLiYo+yJEl99An6BWDj0P4G4EzPMQvAQlU90bU/wiD436SqDlbVTFXNTE9P96ldktRDn6A/BmxJsjnJWmAXcGTJmCPA7d3VNzcBL1XV81X1AnA6yXu6cR8EvrZSxUuSxlszbkBVnUuyFzgKTAGHqup4kj1d/wFgFrgFmAdeAe4YWuKXgYe7vyROLemTJK2ysUEPUFWzDMJ8uO3A0HYBd55n7jPAzMWXKEm6FH4zVpIaZ9BLUuMMeklqnEEvSY0z6CWpcQa9JDXOoJekxhn0ktQ4g16SGmfQS1LjDHpJapxBL0mNM+glqXEGvSQ1zqCXpMYZ9JLUuF5Bn2R7kpNJ5pO86eHe3SME7+v6n01y45L+qSRPJ/n8ShUuSepnbNAnmQL2AzuArcBtSbYuGbYD2NK9dgP3L+m/GzhxydVKkpatzxH9NmC+qk5V1VngMLBzyZidwEM18DiwLsm1AEk2ALcCD6xg3ZKknvoE/Xrg9ND+QtfWd8zvAL8KvH5xJUqSLkWfoM+ItuozJsmHgBer6smxb5LsTjKXZG5xcbFHWZKkPvoE/QKwcWh/A3Cm55ibgQ8neY7BKZ8PJPnsqDepqoNVNVNVM9PT0z3LlySN0yfojwFbkmxOshbYBRxZMuYIcHt39c1NwEtV9XxV/XpVbaiqTd28L1XVR1fyA0iSLmzNuAFVdS7JXuAoMAUcqqrjSfZ0/QeAWeAWYB54Bbhj9UqWJC3H2KAHqKpZBmE+3HZgaLuAO8es8Sjw6LIrlCRdEr8ZK0mNM+glqXEGvSQ1zqCXpMYZ9JLUOINekhpn0EtS4wx6SWqcQS9JjTPoJalxBr0kNc6gl6TGGfSS1DiDXpIaZ9BLUuMMeklqXK+gT7I9yckk80n2jehPkvu6/meT3Ni1b0zyZ0lOJDme5O6V/gCSpAsbG/RJpoD9wA5gK3Bbkq1Lhu0AtnSv3cD9Xfs54Feq6u8DNwF3jpgrSVpFfY7otwHzVXWqqs4Ch4GdS8bsBB6qgceBdUmu7R4Q/hRAVX0POAGsX8H6JUlj9An69cDpof0F3hzWY8ck2QTcADyx7ColSRetT9BnRFstZ0yStwN/BNxTVS+PfJNkd5K5JHOLi4s9ypIk9dEn6BeAjUP7G4AzfcckeQuDkH+4qj53vjepqoNVNVNVM9PT031qlyT10CfojwFbkmxOshbYBRxZMuYIcHt39c1NwEtV9XySAA8CJ6rqt1a0cklSL2vGDaiqc0n2AkeBKeBQVR1PsqfrPwDMArcA88ArwB3d9JuBjwFfTfJM1/bJqppd0U8hSTqvsUEP0AXz7JK2A0PbBdw5Yt6XGX3+XpJ0mfjNWElqnEEvSY0z6CWpcQa9JDXOoJekxhn0ktQ4g16SGmfQS1LjDHpJapxBL0mNM+glqXEGvSQ1zqCXpMYZ9JLUOINekhpn0EtS43oFfZLtSU4mmU+yb0R/ktzX9T+b5Ma+cyVJq2ts0CeZAvYDO4CtwG1Jti4ZtgPY0r12A/cvY64kaRX1OaLfBsxX1amqOgscBnYuGbMTeKgGHgfWJbm251xJ0irqE/TrgdND+wtdW58xfeZKklZRn4eDj3q4d/Uc02fuYIFkN4PTPgDfT3KyR20a7xrg25MuYpz8t0lXoAnx53Pl/OT5OvoE/QKwcWh/A3Cm55i1PeYCUFUHgYM96tEyJJmrqplJ1yGN4s/n5dHn1M0xYEuSzUnWAruAI0vGHAFu766+uQl4qaqe7zlXkrSKxh7RV9W5JHuBo8AUcKiqjifZ0/UfAGaBW4B54BXgjgvNXZVPIkkaKVUjT5mrEUl2d6fFpB86/nxeHga9JDXOWyBIUuMMeklqnEEvSY0z6BuU5B1JfjvJXPf670neMem6pCT/OslPdNv/Mcnnhm+CqNVh0LfpEPAy8G+618vAZyZakTTwn6rqe0neB/xz4PfpboKo1WPQt+ndVXVvdzO5U1X1X4DrJl2UBPxN9+etwP1V9ccMvkGvVWTQt+kH3RETAEluBn4wwXqkN3wrye8y+JfmbJK/gzm06ryOvkFJ3svgn8RvnJf/K+DjVfXsxIqSgCRXAduBr1bVN7rbmf90VX1xwqU1rc9NzfSj5wTwm8C7gXXAS8BHAINeE1VVryR5EXgf8A3gXPenVpFB36Y/Br4LPAV8a7KlSH8ryb3ADPAeBhcIvAX4LHDzJOtqnUHfpg1VtX3SRUgj/AvgBgYHIVTVmTcut9Tq8ZcgbfrzJD896SKkEc7W4BeDBZDkbROu54rgEX2b3gf82yTfBF5l8KSvqqqfmWxZEn/YXXWzLskvAf8O+L0J19Q8g75NOyZdgHQerwL/m8GX+N4D/Oeq+tPJltQ+g75BVfWXk65BOo+/C9zN4Bz9IQahr1XmdfSSLqskAf4ZgyfRzQB/CDxYVf93ooU1zF/GSrqsul/GvtC9zgHvBB5J8psTLaxhHtFLumyS3AV8HPg28ADwv6rqtSQ/Bnyjqt490QIb5Tl6SZfTNcC/XPp7pKp6PcmHJlRT8zyil6TGeY5ekhpn0EtS4wx6NS/JpiR/sYrr//lqrS2tBINeukRV9XOTrkG6EINeV4qpJL+X5HiSLyb58STvTfJ4kmeT/M8k7wRI8miSmW77miTPdds/leQrSZ7p5mzp2r/f/flPurmPJPl6koe7LweR5Jau7ctJ7kvy+Yn8V9AVyaDXlWILsL+qforBvfr/FfAQ8Gvdzd6+Ctw7Zo09wKer6r0MvtG5MGLMDcA9wFYGz+m9Oclbgd8FdlTV+4DpS/0w0nIY9LpSfLOqnum2n6R7+lZV/Z+u7feB949Z4zHgk0l+DfjJqhr1HN6vVNVCVb0OPANsAq4HTlXVN7sxf3DRn0K6CAa9rhSvDm3/DYNHLJ7POf72/423vtFYVf8D+DCDB60fTfKBHu+zhsFtoqWJMeh1pXoJ+Ksk/7jb/xjwxtH9c8A/6rZ/4Y0JSa5jcGR+H3AE6Ht//68D1yXZ1O3/4sWXLS2ft0DQlezjwIEkVwGnGNxNEeBTDB6Q8THgS0PjfxH4aJLXGNyQ67/2eZOq+kGSfw98Icm3ga+s1AeQ+vAWCNJlkOTtVfX97iqc/Qxu4PXbk65LVwZP3UiXxy8leQY4DryDwVU40mXhEb0kNc4jeklqnEEvSY0z6CWpcQa9JDXOoJekxhn0ktS4/w9sRKZqpfBnvgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the bar graph of housing loan status with average value of response_flag\n",
    "inp1.groupby([\"housing\"])[\"response_flag\"].mean().plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Age vs response "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX4AAAEGCAYAAABiq/5QAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjQuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/MnkTPAAAACXBIWXMAAAsTAAALEwEAmpwYAAAU6UlEQVR4nO3df9SfdX3f8ecriSDgUBJDFqIQ9M78MW0Qbz3+KBwKxDGronW0drXedWyc7XhC3HacVN2Bbc7StWdT6NoZtVtsrafMamFdmxIzUfHXvEEoKGzJbEBjmtxGNEQqkuS9P+4rkIQkvYO5vtedfJ6Pc3Ku7+e6v9f3+0rOdV73J9f3+l5XqgpJUjvmDB1AkjRaFr8kNcbil6TGWPyS1BiLX5IaM2/oADPx9Kc/vZYuXTp0DEk6ptx2223fraqFB64/Jop/6dKlTE5ODh1Dko4pSe472HoP9UhSYyx+SWqMxS9JjbH4JakxFn9jtm/fzpVXXsn27duHjiLtx31zdCz+xqxZs4a77rqLj370o0NHkfbjvjk6Fn9Dtm/fztq1a6kq1q5d68xKs4b75mhZ/A1Zs2YNe/bsAWD37t3OrDRruG+OlsXfkE9/+tPs2rULgF27drFu3bqBE0nT3DdHy+JvyHnnnXfYsTSUiy++mDlzputozpw5rFixYuBExzeLvyHebU2z1cTExKOHevbs2cNb3vKWgRMd3yz+htx66637jT//+c8PlETa3wMPPHDYsY4ui78hF198MXPnzgVg7ty5/ndas8Z73/vew451dFn8DZmYmHi0+OfNm+d/pzVrbNq06bBjHV0Wf0MWLFjAJZdcQhIuueQSFixYMHQkCYDFixfvNz7jjDMGStKGY+J6/Dp6JiYm2LRpk7N9zWqeiNAvi78xCxYs4Lrrrhs6hrSfLVu2HHaso8tDPZIGd+CtVb3Var96Lf4kq5LcneTrSd7erZufZF2SDd3ytD4zSJr93vOe9xx2rKOrt+JP8gLgnwAvBZYDr0myDLgKWF9Vy4D13ViSNCJ9zvifB3y5qh6qql3AZ4E3AJcCa7rnrAFe32MGHWBycpILL7yQ2267bego0qM8j3+0+iz+u4HzkyxIcjLwauCZwKKq2gLQLU8/2MZJrkgymWRyamqqx5htueaaa9izZw9XX3310FGkR3ke/2j1VvxVdQ/w68A6YC1wJ7DrCLZfXVXjVTW+cOHCnlK2ZXJykp07dwKwc+dOZ/2aNfxwd7R6/XC3qj5SVedW1fnA94ANwNYkiwG65bY+M+gx11xzzX5jZ/2aLfxwd7T6Pqvn9G55JvBzwMeBm4CJ7ikTwI19ZtBj9s72DzWWhjI2NvboLH/p0qWMjY0NG+g41/d5/H+U5BvA/wDeVlUPANcCK5JsAFZ0Y41AksOOpSG94Q1vAOCNb3zjwEmOf71+c7eqHnenj6raDlzU5/vq4A78Grxfi9ds8qEPfQiAD37wg7z2ta8dOM3xzW/uNuSZz3zmYcfSUDzxYLQs/oY861nP2m/87Gc/e6Ak0v488WC0LP6GfPGLX9xv/IUvfGGgJNL+PPFgtCz+hjzyyCOHHUtqg8UvSY2x+Bvi6ZyarebMmXPYsY4u/3Ub8sIXvvCwY2konmo8WhZ/Q+69997DjqWhWPyjZfE3xA93JYHF3xRnVZLA4pek5lj8ktQYi1+SGmPxS1JjLH5JaozFL0mNsfglqTF933P3nyf5epK7k3w8yZOTzE+yLsmGbnlanxkkSfvrrfiTLAGuBMar6gXAXOBNwFXA+qpaBqzvxpKkEen7UM884KQk84CTge8AlwJrup+vAV7fcwZJ0j56K/6q2gz8JnA/sAX4QVXdDCyqqi3dc7YApx9s+yRXJJlMMjk1NdVXTElqTp+Hek5jenZ/NnAGcEqSN890+6paXVXjVTW+cOHCvmJKUnP6PNRzMfCXVTVVVY8AnwReAWxNshigW27rMYMk6QB9Fv/9wMuSnJzpWz1dBNwD3ARMdM+ZAG7sMYMk6QDz+nrhqvpKkk8AtwO7gK8Bq4GnADckuZzpXw6X9ZVB0sxcf/31bNy4cbD3P/XUU9mxY8ej46c+9amsWrVqsDxjY2OsXLlysPfvW2/FD1BVVwNXH7D6YaZn/5IEwNlnn82dd9756Hjp0qXDhWlAr8Uv6dgwG2a3r3vd69ixYwcrVqzg3e9+99BxjmsWv6RZ4eyzzwaw9EfAa/VIUmMsfklqjMUvSY2x+CWpMRa/JDXG4pekxlj8ktQYi1+SGmPxS1JjLH5JaozFL0mNsfglqTEWvyQ1xuKXpMb0ebP15yS5Y58/O5K8Pcn8JOuSbOiWp/WVQZL0eL0Vf1X9n6o6p6rOAV4MPAR8CrgKWF9Vy4D13ViSNCKjuhHLRcD/q6r7klwKXNCtXwPcArxzRDkGM/Q9TQ9lqPuaHu/3NJVms1Ed438T8PHu8aKq2gLQLU8/2AZJrkgymWRyampqRDEl6fjX+4w/yQnA64BfPZLtqmo1sBpgfHy8eog2UrNldnvBBRc8+viWW24ZLIek4Yxixv/3gdurams33ppkMUC33DaCDDrACSecMHQESQMZRfH/Io8d5gG4CZjoHk8AN44ggzrLly9n+fLl3HzzzUNHkTSQXos/ycnACuCT+6y+FliRZEP3s2v7zCBJ2l+vx/ir6iFgwQHrtjN9lo8kaQB+c1eSGmPxS1JjLH5JaozFL0mNsfglqTEWvyQ1xuKXpMZY/JLUGItfkhpj8UtSYyx+SWqMxS9JjbH4JakxFr8kNcbil6TGWPyS1BiLX5Ia0/etF5+W5BNJ7k1yT5KXJ5mfZF2SDd3ytD4zSJL21/eM/wPA2qp6LrAcuAe4ClhfVcuA9d1YkjQivRV/klOB84GPAFTVj6vq+8ClwJruaWuA1/eVQZL0eH3O+J8FTAH/NcnXknw4ySnAoqraAtAtTz/YxkmuSDKZZHJqaqrHmJLUlj6Lfx5wLvA7VfUi4IccwWGdqlpdVeNVNb5w4cK+MkpSc46o+LsZ+0x9G/h2VX2lG3+C6V8EW5Ms7l5vMbDtSDJIkn4yMyr+JK9I8g2mP5wlyfIkv324barqr4BvJXlOt+oi4BvATcBEt24CuPGJBJckPTHzZvi8/wT8PaZLm6q6M8n5M9huJfCxJCcA3wTeyvQvmxuSXA7cD1x2xKklSU/YTIufqvpWkn1X7Z7BNncA4wf50UUzfV9J0tE10+L/VpJXANXN3q+kO+wjSTq2zPTD3X8KvA1YwvSHtud0Y0nSMWZGM/6q+i7wSz1nkSSNwIyKP8l1B1n9A2CyqjwrR5KOITM91PNkpg/vbOj+/BQwH7g8yft7SSZJ6sVMP9wdAy6sql0ASX4HuBlYAdzVUzZJUg9mOuNfAuz7rd1TgDOqajfw8FFPJUnqzUxn/P8BuCPJLUCYvurm+7pLOHy6p2ySpB7M9KyejyT5M+CXgXuZPszz7ar6IfCOHvNJko6ymZ7V84+BVcAzgDuAlwFfAi7sLZkkqRczPca/CngJcF9V/QzwIqavtS9JOsbMtPh/VFU/AkhyYlXdCzznb9hGkjQLzfTD3W8neRrwx8C6JA8A3+krlCSpPzP9cPcN3cNrknwGeCqwtrdUkqTezPiyzHtV1Wf7CCJJGo0+77krSZqFLH5JaswRH+o5Ekk2AQ8yfbeuXVU1nmQ+8IfAUmAT8PNV9UCfOSRJjxnFjP9nquqcqtp7C8argPVVtQxY340lSSPS64z/EC4FLugerwFuAd45QA5pcNdffz0bN24cOsassPffYdWqVQMnmR3GxsZYuXJlL6/dd/EXcHOSAj5YVauBRVW1BaCqtiQ5/WAbJrkCuALgzDPP7DmmNIyNGzey4etf48yn7B46yuBOeGT6AMTD900OnGR49++c2+vr9138r6yq73Tlvi7JvTPdsPslsRpgfHy8+gooDe3Mp+zmXefuGDqGZpH33X5qr6/f6zH+qvpOt9wGfAp4KbA1yWKAbrmtzwySpP31VvxJTknyt/Y+Bl4F3A3cBEx0T5sAvGevJI1Qn4d6FgGfSrL3ff6gqtYm+SpwQ5LLgfuBy3rMAPgB2r78AG1/fX6AJs1WvRV/VX0TWH6Q9duBi/p634PZuHEjd9x9D7tPnj/Kt52V5vx4+uOS2765deAkw5v70PeGjiANYojTOQex++T5/PVzXz10DM0iJ937p0NHkAbhJRskqTEWvyQ1xuKXpMZY/JLUGItfkhpj8UtSYyx+SWqMxS9JjbH4JakxFr8kNcbil6TGWPyS1BiLX5IaY/FLUmMsfklqTO/Fn2Rukq8l+ZNuPD/JuiQbuuVpfWeQJD1mFDP+VcA9+4yvAtZX1TJgfTeWJI1Ir8Wf5BnAzwIf3mf1pcCa7vEa4PV9ZpAk7a/vGf/7gX8F7Nln3aKq2gLQLU8/2IZJrkgymWRyamqq55iS1I7eij/Ja4BtVXXbE9m+qlZX1XhVjS9cuPAop5OkdvV5s/VXAq9L8mrgycCpSX4f2JpkcVVtSbIY2NZjBgA2b97M3Id+4M21tZ+5D21n8+ZdQ8eQRq63GX9V/WpVPaOqlgJvAv5XVb0ZuAmY6J42AdzYVwZJ0uP1OeM/lGuBG5JcDtwPXNb3Gy5ZsoS/engef/3cV/f9VjqGnHTvn7JkyaKhY0gjN5Lir6pbgFu6x9uBi0bxvtJst3nzZn744Fzed/upQ0fRLHLfg3M5ZfPm3l7fb+5KUmOGONQjqbNkyRIe3rWFd527Y+gomkXed/upnLhkSW+v74xfkhpj8UtSYyx+SWqMxS9JjbH4JakxFr8kNcbil6TGWPyS1BiLX5Ia08w3d+c+9D0vywzM+dH0N0T3PNlrw8x96HuAF2lTe5oo/rGxsaEjzBobNz4IwNizLDxY5L6hJjVR/CtXrhw6wqyxatUqAD7wgQ8MnETSUDzGL0mNsfglqTEWvyQ1prdj/EmeDHwOOLF7n09U1dVJ5gN/CCwFNgE/X1UP9JVDmu3u3+kduAC2PjQ9D1108p6Bkwzv/p1zWdbj6/f54e7DwIVVtTPJk4Bbk/wZ8HPA+qq6NslVwFXAO3vMIc1anlX0mB9v3AjAiWf5b7KMfveN3oq/qgrY2Q2f1P0p4FLggm79GqbvxWvxq0mecfYYzzgbnV6P8SeZm+QOYBuwrqq+Aiyqqi0A3fL0Q2x7RZLJJJNTU1N9xpSkpvRa/FW1u6rOAZ4BvDTJC45g29VVNV5V4wsXLuwtoyS1ZiRn9VTV95k+pHMJsDXJYoBuuW0UGSRJ03or/iQLkzyte3wScDFwL3ATMNE9bQK4sa8MkqTH6/OsnsXAmiRzmf4Fc0NV/UmSLwE3JLkcuB+4rMcMkqQD9HlWz18ALzrI+u3ARX29ryTp8PzmriQ1xuKXpMZY/JLUGItfkhpj8UtSYyx+SWqMxS9JjbH4JakxFr8kNcbil6TGWPyS1BiLX5IaY/FLUmMsfklqjMUvSY2x+CWpMRa/JDWmz3vuPjPJZ5Lck+TrSVZ16+cnWZdkQ7c8ra8MkqTH63PGvwv4l1X1POBlwNuSPB+4ClhfVcuA9d1YkjQivRV/VW2pqtu7xw8C9wBLgEuBNd3T1gCv7yuDJOnxRnKMP8lSpm+8/hVgUVVtgelfDsDph9jmiiSTSSanpqZGEVOSmtB78Sd5CvBHwNurasdMt6uq1VU1XlXjCxcu7C+gJDWm1+JP8iSmS/9jVfXJbvXWJIu7ny8GtvWZQZK0vz7P6gnwEeCeqvqP+/zoJmCiezwB3NhXBknS46Wq+nnh5KeBzwN3AXu61e9i+jj/DcCZwP3AZVX1vcO91vj4eE1OTvaSc1Suv/56Nm7cOHSMRzOMjY0NmmNsbIyVK1cOmkGPmQ3752zZN/dmOB72zyS3VdX4gevn9fWGVXUrkEP8+KK+3leHd9JJJw0dQToo983R6W3GfzQdDzN+SRq1Q834vWSDJDXG4pekxlj8ktQYi1+SGmPxS1JjLH5JaozFL0mNsfglqTHHxBe4kkwB9w2d4zjydOC7Q4eQDsJ98+g6q6oed3njY6L4dXQlmTzYt/mkoblvjoaHeiSpMRa/JDXG4m/T6qEDSIfgvjkCHuOXpMY445ekxlj8ktQYi1+SGmPxS1JjLP7jWJKlSe5J8qEkX09yc5KTkpyT5MtJ/iLJp5KcNnRWtSHJv0uyap/xv09yZZJ3JPlqt0/+m+5npyT5n0nuTHJ3kl8YLvnxxeI//i0D/nNV/V3g+8AbgY8C76yqnwLuAq4eLp4a8xFgAiDJHOBNwFam99OXAucAL05yPnAJ8J2qWl5VLwDWDpL4OGTxH//+sqru6B7fBjwbeFpVfbZbtwY4f4hgak9VbQK2J3kR8Crga8BL9nl8O/Bcpn8R3AVcnOTXk5xXVT8YJvXxZ97QAdS7h/d5vBt42kA5pL0+DPwK8LeB3wUuAn6tqj544BOTvBh4NfBrSW6uqn87yqDHK2f87fkB8ECS87rxLwOfPczzpaPtU0wfxnkJ8Ofdn3+U5CkASZYkOT3JGcBDVfX7wG8C5w4V+HjjjL9NE8B/SXIy8E3grQPnUUOq6sdJPgN8v6p2AzcneR7wpSQAO4E3A2PAbyTZAzwC/LOhMh9vvGSDpJHqPtS9HbisqjYMnadFHuqRNDJJng9sBNZb+sNxxi9JjXHGL0mNsfglqTEWvyQ1xuKXpMZY/GpSprn/q0nu+GrGPlcr/W2mzyP/1zO9ImSSTd01Y/5392esW39WkvXda6xPcma3/r8luS7JF5N8M8k/6NYvTvK5JHd0r39et/5VSb6U5PYk/33vt1ilPlj8as1z6K5OCizhyK4IuaOqXgr8FvD+bt1vAR/trnT6MeC6fZ6/GPhp4DXAtd26fwj8eVWdAywH7kjydOA9wMVVdS4wCfyLo/h3lvZj8as191XVl5m+GuSRXhHy4/ssX949fjnwB93j32O66Pf646raU1XfABZ1674KvDXJNcALq+pB4GXA84EvJLmD6UtqnHWU/r7S43itHrXmh90yHPkVIff9tuOhvvm47/p9r4wagKr6XPc/i58Ffi/JbwAPAOuq6heP+G8jPQHO+NWqJ3JFyF/YZ/ml7vEXmb6ZCMAvAbce7k2TnAVsq6oPMX1TknOBLwOv3Odzg5OT/J2f9C8oHYozfjWpqp7IFSFPTPIVpidMe2fnVwK/m+QdwBR/85VOLwDekeSR7j3fUlVTSX4F+HiSE7vnvQf4vz/Z31I6OK/VI81Akk3AeFV9d+gs0k/KQz2S1Bhn/JLUGGf8ktQYi1+SGmPxS1JjLH5JaozFL0mN+f9sCRn/Wh0ODQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the boxplot of age with response_flag\n",
    "sns.boxplot(data=inp1, x=\"response\",y=\"age\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##### making buckets from age columns "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    50-60\n",
       "1    40-50\n",
       "2    30-40\n",
       "3    40-50\n",
       "4    30-40\n",
       "Name: age, dtype: category\n",
       "Categories (5, object): ['<30' < '30-40' < '40-50' < '50-60' < '60+']"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#create the buckets of <30, 30-40, 40-50 50-60 and 60+ from age column.\n",
    "pd.cut(inp1.age[:5],[0, 30, 40, 50, 60, 9999], labels= [\"<30\",\"30-40\",\"40-50\",\"50-60\", \"60+\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    58.0\n",
       "1    44.0\n",
       "2    33.0\n",
       "3    47.0\n",
       "4    33.0\n",
       "Name: age, dtype: float64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1.age.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30-40    0.391090\n",
       "40-50    0.248688\n",
       "50-60    0.178406\n",
       "<30      0.155555\n",
       "60+      0.026262\n",
       "Name: age_group, dtype: float64"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1[\"age_group\"]=pd.cut(inp1.age,[0, 30, 40, 50, 60, 9999], labels= [\"<30\",\"30-40\",\"40-50\",\"50-60\", \"60+\"])\n",
    "inp1.age_group.value_counts(normalize= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the percentage of each buckets and average values of response_flag in each buckets. plot in subplots.\n",
    "plt.figure(figsize=[10,4])\n",
    "plt.subplot(1, 2, 1)\n",
    "inp1.age_group.value_counts(normalize= True).plot.bar()\n",
    "plt.subplot(1, 2, 2)\n",
    "inp1.groupby(['age_group'])['response_flag'].mean().plot.bar()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plot the bar graph of job categories with response_flag mean value.\n",
    "inp1.groupby(['job'])['response_flag'].mean().plot.barh()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Segment-6, Multivariate analysis "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Education vs marital vs response "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=6df4bf1d-6da1-4cf4-a831-27c577d2573d style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('6df4bf1d-6da1-4cf4-a831-27c577d2573d').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>marital</th>\n",
       "      <th>divorced</th>\n",
       "      <th>married</th>\n",
       "      <th>single</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>education</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>primary</th>\n",
       "      <td>0.138852</td>\n",
       "      <td>0.075601</td>\n",
       "      <td>0.106808</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>secondary</th>\n",
       "      <td>0.103559</td>\n",
       "      <td>0.094650</td>\n",
       "      <td>0.129271</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>tertiary</th>\n",
       "      <td>0.137415</td>\n",
       "      <td>0.129835</td>\n",
       "      <td>0.183737</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unknown</th>\n",
       "      <td>0.142012</td>\n",
       "      <td>0.122519</td>\n",
       "      <td>0.162879</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "marital    divorced   married    single\n",
       "education                              \n",
       "primary    0.138852  0.075601  0.106808\n",
       "secondary  0.103559  0.094650  0.129271\n",
       "tertiary   0.137415  0.129835  0.183737\n",
       "unknown    0.142012  0.122519  0.162879"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res=pd.pivot_table(data=inp1, index=\"education\", columns=\"marital\", values=\"response_flag\")\n",
    "res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#create heat map of education vs marital vs response_flag\n",
    "sns.heatmap(res, annot= True, cmap=\"RdYlGn\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(res, annot= True, cmap=\"RdYlGn\", center= 0.117)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Job vs marital vs response "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div><div id=b358885a-bca8-44f9-9ee3-b9a523ec3c56 style=\"display:none; background-color:#9D6CFF; color:white; width:200px; height:30px; padding-left:5px; border-radius:4px; flex-direction:row; justify-content:space-around; align-items:center;\" onmouseover=\"this.style.backgroundColor='#BA9BF8'\" onmouseout=\"this.style.backgroundColor='#9D6CFF'\" onclick=\"window.commands?.execute('create-mitosheet-from-dataframe-output');\">See Full Dataframe in Mito</div> <script> if (window.commands?.hasCommand('create-mitosheet-from-dataframe-output')) document.getElementById('b358885a-bca8-44f9-9ee3-b9a523ec3c56').style.display = 'flex' </script> <table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>marital</th>\n",
       "      <th>divorced</th>\n",
       "      <th>married</th>\n",
       "      <th>single</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>job</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>admin.</th>\n",
       "      <td>0.120160</td>\n",
       "      <td>0.113383</td>\n",
       "      <td>0.136153</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>blue-collar</th>\n",
       "      <td>0.077644</td>\n",
       "      <td>0.062778</td>\n",
       "      <td>0.105760</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>entrepreneur</th>\n",
       "      <td>0.083799</td>\n",
       "      <td>0.075843</td>\n",
       "      <td>0.113924</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>housemaid</th>\n",
       "      <td>0.097826</td>\n",
       "      <td>0.072527</td>\n",
       "      <td>0.166667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>management</th>\n",
       "      <td>0.127928</td>\n",
       "      <td>0.126228</td>\n",
       "      <td>0.162254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>services</th>\n",
       "      <td>0.091241</td>\n",
       "      <td>0.074105</td>\n",
       "      <td>0.117696</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>student</th>\n",
       "      <td>0.166667</td>\n",
       "      <td>0.185185</td>\n",
       "      <td>0.293850</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>technician</th>\n",
       "      <td>0.083243</td>\n",
       "      <td>0.102767</td>\n",
       "      <td>0.132645</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unemployed</th>\n",
       "      <td>0.157895</td>\n",
       "      <td>0.132695</td>\n",
       "      <td>0.195000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unknown</th>\n",
       "      <td>0.058824</td>\n",
       "      <td>0.103448</td>\n",
       "      <td>0.176471</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table></div>"
      ],
      "text/plain": [
       "marital        divorced   married    single\n",
       "job                                        \n",
       "admin.         0.120160  0.113383  0.136153\n",
       "blue-collar    0.077644  0.062778  0.105760\n",
       "entrepreneur   0.083799  0.075843  0.113924\n",
       "housemaid      0.097826  0.072527  0.166667\n",
       "management     0.127928  0.126228  0.162254\n",
       "retired        0.283688  0.220682  0.120370\n",
       "self-employed  0.158273  0.079637  0.191874\n",
       "services       0.091241  0.074105  0.117696\n",
       "student        0.166667  0.185185  0.293850\n",
       "technician     0.083243  0.102767  0.132645\n",
       "unemployed     0.157895  0.132695  0.195000\n",
       "unknown        0.058824  0.103448  0.176471"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "res=pd.pivot_table(data=inp1, index=\"job\", columns=\"marital\", values=\"response_flag\")\n",
    "res"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#create the heat map of Job vs marital vs response_flag.\n",
    "sns.heatmap(res, annot= True, cmap=\"RdYlGn\", center= 0.117)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Education vs poutcome vs response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#create the heat map of education vs poutcome vs response_flag.\n",
    "res=pd.pivot_table(data=inp1, index=\"education\", columns=\"poutcome\", values=\"response_flag\")\n",
    "sns.heatmap(res, annot= True, cmap=\"RdYlGn\", center= 0.117)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.2307785593014795"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inp1[inp1.pdays>0].response_flag.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "res=pd.pivot_table(data=inp1, index=\"education\", columns=\"poutcome\", values=\"response_flag\")\n",
    "sns.heatmap(res, annot= True, cmap=\"RdYlGn\", center= 0.2308)\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
