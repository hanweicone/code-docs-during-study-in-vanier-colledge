## Basic Characteristics of Object Oriented Systems
- Classes and Objects
- Methods and Messages
- Encapsulation and Information Hiding
- Inheritance
- Polymorphism
### Classes, Objects, Methods, and Messages

The basic building block of the system is the object. Objects are instances of classes. Classes are templates that we use to 
define both the data and processes that each object contains. Each object has attributes that describe data about the object.
Objects have state, which is defined by the value of its attributes and its relationships with other objects at a particular
point in time. And each object has methods, which specify what processes the object can perform. A message is essentially a
function or procedure call from one object to another object.

### Encapsulation and Information Hiding

Encapsulation is the mechanism that combines the processes and data into a single object. 
Information hiding suggests that only the information required to use an object be available outside the object; 
that is, information hiding is related to the visibility of the methods and attributes (see Chapter 5).  The only communication between 
objects should be through an object’s methods. The fact that we can use an object by sending a message 
that calls methods is the key to reusability because it shields the internal workings of the object from changes in the outside system,
and it keeps the system from being affected when changes are made to an object.

### Polymorphism and Dynamic Binding
Polymorphism means having the ability to take several forms. By supporting polymorphism,
object-oriented systems can send the same message to a set of objects, which can be interpreted differently by different classes of objects. Based on encapsulation and information
hiding, an object does not have to be concerned with how something is done when using other
objects. It simply sends a message to an object and that object determines how to interpret the
message. This is accomplished through the use of dynamic binding.

Dynamic binding refers to the ability of object-oriented systems to defer the data typing
of objects to run time.

## object-oriented systems development
all object-oriented systems development approaches are
use-case driven, architecture-centric, and iterative and incremental. Use cases, described in
Chapter 4, form the foundation on which the business information system is created. From
an architecture-centric perspective, structural modeling supports the creation of an internal
structural or static view of a business information system in that it shows how the system is
structured to support the underlying business processes. Finally, as with business process and
functional modeling, you will find that you will need to not only iterate across the structural
models (described in this chapter), but you will also have to iterate across all three architectural
views (functional, structural, and behavioral) to fully capture and represent the requirements
for a business information system.


Behavioral models describe the internal dynamic aspects of an information system that supports business processes in an organization
Key UML behavioral models are: sequence diagrams and behavioural state machines
sequence diagrams:Illustrate the objects that participate in a use-case,Show the messages that pass between objects for a particular use-case

The behavioral state machine is a dynamic model that shows the different states of the object and what events cause the object to change from one state to another, along with its responses and actions.
## object-oriented Analysis and Design Foundation
- Use-case driven
- Architecture centric
- Iterative and incremental

## object-oriented Analysis and Design-Combining Three Views
### Functional:
- use case diagrams
### Static:
- class diagrams 
- object diagrams
### Dynamic:
- sequence diagrams: elements how it works(read lec 6)
- behavioral state machines (state chart diagrams) elements how it works(read lec 6)

## Avoid Classic Design Mistakes

### Reducing design time:
If time is short, there is a temptation to jump into programming. This results in missing important details that have to be investigated later at
a much higher time cost (usually, at least 10 timesLonger)

 **Solution:** If time pressure is intense, use rapid application development (RAD) techniques and timeboxing to eliminate functionality or move it into future versions.

### Feature creep:
- Even if you are successful at avoiding scope creep, about 25% of system requirements will still change. Changes—big and small—can significantly
- increase time and cost.

 **Solution:** Ensure that all changes are vital and that the users are aware of the impact on cost and time. Try to move proposed changes into future versions.
### Silver bullet syndrome
-	Analysts sometimes believe the
-	marketing claims that some design tools solve all problems and magically reduce time and costs. 
-	No one tool or technique can eliminate overall time or
 
 **Solution**	If a design tool has claims that appear too good to be true, just say no.
 ### Switching tools in mid-project
-	Sometimes, analysts switch to what appears to be a better tool during design in the hopes of saving time or costs.
-	 Usually, any benefits are outweighed by the need to learn the new tool. 
 
 **Solution** 
-	This also applies to even “minor” upgrades to current tools.
-	Solution: Don’t switch or upgrade unless there is a
-	compelling need for specific features in the new tool and it helps with the efficiency. 

## DESIGN STRATEGIES

### Custom Development
-	Building from scatch. 
-	Allows for meeting highlyspecialized requirements.
-	Allows flexibility and creativity in solving problems
-	Easier to change components
-	Builds personnel skills
-	May stretch company’s resources
-	May add significant risk

### Packaged Software
-	Software already written
-	May be more efficient. Don`t reinvent the wheel.
-	May be more thoroughly tested and proven
-	May range from components to tools to whole enterprise systems
-	Must accept functionality provided
-	May require change in how the firm does business
-	May require significant “customization” or “workarounds”

### System Integration
-	The process of combining packages, legacy systems, and new software
-	Key challenge is integrating data
-	Write data in the same format
-	Revise existing data formats
-	Develop “object wrappers”

### Outsourcing
-	Hire external firm to create system
-	May have more skills
-	May extend existing resources
-	Never outsource what you don’t understand
-	Carefully choose vendor
	Prepare contract and payment style carefully
	
 **What is normalization?
When normalization?
What is denormalization?
When denormalization?(page 346)** 
## Problems with RDBMS (Relational database management system)
-	To access data in multiple tables, the tables must be joined
-	This can result in many database operations and lead to  huge tables and slow processing
### Speeding up access
-	Denormalization – Adds data from one table to another in order to speed processing and eliminate a join operation
-	Example: Add customer last name to order table to avoid joining order to customer to get just last name
## Physical Architecture
### Software Components
-	**Data Storage**: Most information systems require data to be stored and retrieved 

-	**Data Access Logic**: the processing required to access data, often meaning database queries in Structured Query Language (SQL).

-	**Application logic**: the logic documented in the DFDs, use cases  and functional requirements.

-	**Presentation logic**: The display of information to the user and the acceptance of the user’s commands (the user interface)

### Hardware Components
-	Client computers
-	Servers
- Connecting network

## server Based Architecture
very first computing architectures were server based,
with the server (usually, a central mainframe computer) performing all
four application functions. 

The clients (usually, terminals) enabled users to send
and receive messages to and from the server computer
Limitations? Over loaded systems as the demand increased

## Client Based Architecture
The clients are microcomputers on a local area network, and the server is a server computer on the same network. 

The application software on the client computers is responsible for the presentation logic, the application logic, 
and the data access logic;
### Client based Analysis
This simple architecture often works very well in situations with low numbers of users or limited data access requirements. 

The fundamental is that all data on the server must travel to the client for processing.

## Client-Server Architectures
The client is responsible for the presentation logic, whereas the server is responsible for the data access logic and data storage. 

The application logic may reside on the client, reside on the server, or be split between both.
## 2-Tiered Architecture
client:presentation logic, the application logic.

server:the data access logic,data storeage.

## 3-Tiered Architecture
the soft ware on the client computer is responsible for presentation logic, an application server (or
servers) is responsible for the application logic, and a separate database server (or servers) is
responsible for the data access logic and data storage

## N-Tiered Architecture
the client is responsible for presentation, database servers are responsible for the data access logic and
data storage, and the application logic is spread across two or more diff erent sets of servers.
