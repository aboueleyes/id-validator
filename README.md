# id-validator
Egyptian national ID validator and data-extractor API

## Project Setup

```bash
> git clone git@github.com:aboueleyes/id-validator.git # clone the repo
> cd id-validator/ # navigate to the directory
> sudo pip3 install -r requiremnts.txt   # <- just installing django
> cd idVaildator/
> python manage.py runserver # run the server it will run on port 8000 
> curl http://127.0.0.1:8000/core/{id} # replace id with your desired natinol id
```

## Ruunig Tests

```bash
(id-validator/idVaildator)> ./manage.py test
```
```bash
(/)> ./test.sh
```
[Regex Tests](https://regexr.com/6hl0q)


## Sample Output

```bash
> curl http://127.0.0.1:8000/core/12388947 
```
*output*

```json
{"error": "Invalid ID"}
```

```bash
>  curl  http://127.0.0.1:8000/core/30103211203135
```
*output* 

```json
{"birthDate": "2001-03-21", "gender": "Male", "governrate": "Dakahlia"}

```
```bash
> curl http://127.0.0.1:8000/core/29903211707122
```

```json
{"birthDate": "1999-03-21", "gender": "Female", "governrate": "Monoufia"}
```

## ID Format 
```
2 - 990115 - 01 - 0192 - 1

x - yymmdd - ss - iiig - z
```


- x (2) is the birth century (2 represent 1900 to 1999, 3 represent 2000 to 2099 .. etc)

- yymmdd (200115) is the date of birth, yy(99) year,mm(01) month, dd(15) day

- ss(01) birth governorate coda (88 for people who born in a foreign country, 01 for who born in Cairo, ...etc )

- iiig(0192) the sequence in the computer between births in this birthday and

 - g(2) represent the gender (2,4,6,8 for females and 1,3,5,7,9)

 - z(1) number Ministry of Interior added it to validate if the National ID fake or not (1 to 9)

## Project Decisions

- Used [Regex](https://regexr.com/6hl0q) to check the validity of the id
- If the id century is less than 1900 or greater than 2100 it will return error assuming no one before `1900` is using our service 
and the code must be updated after `78` years from now :D.
- if the id has a year greater than the current year the api wouldn't report that (my design choise) but it can be handeld easily. 
- The unit tests are very basic but I guess they do the job.

