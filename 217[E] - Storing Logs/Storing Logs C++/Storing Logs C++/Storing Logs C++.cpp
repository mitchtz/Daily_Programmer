// Storing Logs C++.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	//Take in on command line the name of the file to open and process
	//Check to see if number of command line inputs are correct
	//Not enough inputs on command line
	if (argc < 2){
		cout << "Command line argument must be the name of the input file to process" << endl;
		return 0;
	}
	//Too many command line arguments
	else if (argc > 2)
	{
		cout << "Command line argument must only be the name of the input file to process" << endl;
		return 0;
	}
	//Create array to store stacks of logs already in storage
	int *storage = NULL;
	//Create int to store grid size (one side length)
	int grid_size;
	//Create int to store number of logs left to place
	int logs_to_place;
	//Temp variable to store line from file
	string line;
	//Name of file to open (passed in on command line
	ifstream myfile(argv[1]);
	/*Open file and extract grid size, logs to place, and the storage array*/
	if (myfile.is_open())
	{
		/*Get number of rows/columns in storage*/
		//Get next line from input file
		getline(myfile, line);
		//Convert grid size from string to int
		grid_size = stoi(line);
		cout << "Grid size = " << grid_size << endl;
		
		/*Get number of logs to place*/
		//Get next line from input file
		getline(myfile, line);
		//Convert number of logs to place into int from string
		logs_to_place = stoi(line);
		cout << "Logs left to place = " << logs_to_place << endl;
		
		//Allocate memory to the array to create a 1d array to represent the storage grid
		storage = (int *)malloc(sizeof(int) * (grid_size*grid_size));
		/*Read grid and store into 1d array*/
		//For iterating through the storage grid
		int stor_iter = 0;
		while (getline(myfile, line))
		{
			//Take line and split, convert to int. Each line has one row of the storage grid
			//For iterating through the row
			int row_iter = 0;
			//Feed line to ssin
			stringstream ssin(line);
			//Iterate through the line, place numbers into storage array
			while (ssin.good() && row_iter < grid_size)
			{
				//Store seperated number in storage array
				ssin >> storage[stor_iter];
				//Iterate storage and row
				stor_iter++;
				row_iter++;
			}
		}

		/*Now iterate through array and add one log to smallest stack until there are no logs left to place*/
		//Store smallest number
		int smallest;
		//Store smallest number index
		int smallest_index;
		while (logs_to_place > 0)
		{
			//Reset smallest
			//Set smallest to first stack in storage
			smallest = storage[0];
			//Set smallest index to first stack also
			smallest_index = 0;
			//Iterate through storage array, find smallest index, start index at 1 since smallest index is set to 0 initially
			for (int i = 1; i < (grid_size*grid_size); i++)
			{
				//Check if this stack is smaller
				if (storage[i] < smallest)
				{
					//Set new smallest and smallest index
					smallest = storage[i];
					smallest_index = i;
				}
			}
			//Add log to smallest stack
			storage[smallest_index]++;
			//Decrement logs left to place
			logs_to_place--;
		}

		//Print storage if array was filled
		if (storage != NULL)
		{
			for (int i = 0; i < grid_size; i++)
			{
				for (int j = 0; j < grid_size; j++)
				{
					cout << storage[(i * grid_size) + j] << " ";
				}
				cout << endl;
			}
		}
		cout << endl;
		myfile.close();
	}

	else cout << "Unable to open file" << endl;

	//Free storage allocated to storage array
	free(storage);

	return 0;
}

