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

```
> ./manage.py test
```

## Sample Output

```
> curl http://127.0.0.1:8000/core/12388947 
```
*output*

```
{"error": "Invalid ID"}
```

```
>  curl  http://127.0.0.1:8000/core/30103211203135
```
*output* 

```
{"birthDate": "2001-03-21", "gender": "Male", "governrate": "Dakahlia"}

```


## Project Decisions

- Used [Regex](https://regexr.com/6hl0q) to check the validity of the id
- If the id century is less than 1900 or greater than 2100 it will return error assuming no one before `1900` is using our service 
and the code must be updated after `78` years from now :D.
- if the id has a year greater than the current year the api wouldn't report that (my design choise) but it can be handeld easily. 
- The unit tests are very basic but I guess they do the job.
