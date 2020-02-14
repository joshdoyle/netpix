# SEI Project Proposal 3
## Idea
* Users can create collections of Netflix shows
* Users can search for Netflix shows and get info about show.
	- Data is provided by the external api uNoGS (unofficial Netflix online Global Search) allows anyone to search the global Netflix catalog.
* User will have to be authenticated
* Styling by Semantic-UI-React

#### Nice to have bonuses if time allows
* Users can add other users collections to their collections
* Users can comment on collections
* User has favorite categories
* Collections can be rated
* Shows can be rated
* User can create a schedule for when they want to watch those shows.

## Models
**Users**
```
class User(Model):
  username = CharField(unique=True)
  email = CharField(unique=True) 
  password = CharField()
```

**Collection**
```
class Collection(Model):
	user = ForeignKeyField(User, backref='Collection')
	name = CharField()
	description = CharField()
	category = CharField()
```
**ShowCollection**
```
class ShowCollection(Model):
	collection_id: ForeignKeyField(Collection, backref='ShowCollection')
	show_id: ForeignKeyField(Show, backref='ShowCollection')
	user_description = CharField(unique=True)
```
**Show**
```
class Show(Model):
	apiShow_id = CharField(unique=True)
	apiEpisode_id = CharField(unique=True)
```
## Wireframes


## Routes

   NAME   |     PATH                 |   HTTP VERB     |            PURPOSE                   
----------|--------------------------|-----------------|-------------------------------------- 
 **Show Collection**
 Index    | /showcollection          |      GET        | Displays all show collections        
 New      | /showcollection/new      |      GET        | Shows new form for show collections  
 Create   | /showcollection          |      POST       | Creates a new show collection        
 Show     | /showcollection/:id      |      GET        | Shows one specified show collection  
 Edit     | /showcollection/:id/edit |      GET        | Shows edit form for  show collection 
 Update   | /showcollection/:id      |      PUT        | Updates a particular show collection 
 Destroy  | /showcollection/:id      |      DELETE     | Deletes a particular show collection   
  **Show**
 Index    | /show                    |      GET        | Displays all shows             
 Show     | /show/:id                |      GET        | Shows one specified show  
 Edit     | /show/:id/edit           |      GET        | Shows edit form for show 
 Update   | /show/:id                |      PUT        | Updates a particular show 
 Destroy  | /show/:id                |      DELETE     | Deletes a particular show   
  **User**
 Index    | /user                    |      GET        | Displays all users(bonus?)        
 New      | /user/new                |      GET        | Shows new form for users  
 Create   | /user                    |      POST       | Creates a new user        
 Show     | /user/:id                |      GET        | Shows one specified user  
 Edit     | /user/:id/edit           |      GET        | Shows edit form for user 
 Update   | /user/:id                |      PUT        | Updates a particular user 
 Destroy  | /user/:id                |      DELETE     | Deletes a particular user    

