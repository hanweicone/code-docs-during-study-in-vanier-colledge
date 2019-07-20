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

## Client-Server Benefits
- Scalable
- Support multiple clients and servers
- Multiple servers make for a generally more reliable network
## Client-Server Limitations
- Complexity
- Updating the network computers is more complex
- Development and Installation 
  	- different on client and server
	- training for developers
## functional requirement
-	what the software should do ( functional requirements): A functional requirement
-	relates directly to a process the system has to perform as a part of supporting a user task and/or information it needs to provide as the user is performing a task.

## NonFunctional Requirements:
-	characteristics the system should have (nonfunctional requirements); 
-	How the system should be built (system requirements). 

## Conversion Location
Conversion location refers to the parts of the organization that are converted when the conversion
occurs. Often, parts of the organization are physically located in different offices(e.g., Toronto,
Atlanta, Los Angeles). In other cases, location refers to different organizational units located in
Change management.
## How to covert old system to new ?
**Conversion is the technical process of replacing the old system with the new one.  Designers select the method, timing, and location of the conversion process.**

There are three major steps to the conversion plan before commencement of operations:
Install hardware, install software, and convert data (Figure 13-2). Although it may be possible
to do some of these steps in parallel, usually they must be done sequentially at any one location.

**The first step** in the conversion plan is to buy and install any needed hardware. In many
cases, no new hardware is needed, but sometimes the project requires new hardware such as
servers, client computers, printers, and networking equipment. It is critical to work closely
with vendors who are supplying needed hardware and software to ensure that the deliveries
are coordinated with the conversion schedule so that the equipment is available when it is
needed. Nothing can stop a conversion plan in its tracks as easily as the failure of a vendor to
deliver needed equipment.

Once the hardware is installed, tested, and certified as being operational, **the second step**
is to install the software. This includes the to-be system under development and, sometimes,
additional software that must be installed to make the system operational. At this point, the
system is usually tested again to ensure that it operates as planned.

**The third step** is to convert the data from the as-is system to the to-be system. Data conversion
is usually the most technically complicated step in the migration plan. Often, separate programs
must be written to convert the data from the as-is system to the new formats required in the to-be
system and store it in the to-be system fi les and databases. Th is process is of en complicated by the
fact that the fi les and databases in the to-be system do not exactly match the fi les and databases in
the as-is system (e.g., the to-be system may use several tables in a database to store customer data
that were contained in one fi le in the as-is system). Formal test plans are always required for data
conversion efforts (see Chapter 12).Conversion can be thought of along

## Conversion Style
The conversion style is the way users are switched between the old and new systems. Th ere
are two fundamentally different approaches to the style of conversion: direct conversion and
parallel conversion.
### Direct Conversion
Direct Conversion With direct conversion (sometimes called cold turkey, big bang, or
abrupt cutover), the new system instantly replaces the old system. Th e new system is turned
on, and the old system is immediately turned off . Th is is the approach that we are likely to use
when we upgrade commercial soft ware (e.g., Microsoft Word) from one version to another;
we simply begin using the new version and stop using the old version.

Direct conversion is the simplest and most straightforward. However, it is the most risky
because any problems with the new system that have escaped detection during testing can
seriously disrupt the organization.
### Parallel Conversion
Parallel Conversion With parallel conversion, the new system is operated side by side with
the old system; both systems are used simultaneously. For example, if a new accounting
system is installed, the organization enters data into both the old system and the new system
and then carefully compares the output from both systems to ensure that the new system is
performing correctly. Aft er some time period (oft en one to two months) of parallel operation
and intense comparison between the two systems, the old system is turned off and the organization
continues using the new system.

This approach is more likely to catch any major bugs in the new system and prevent the
organization from suff ering major problems. If problems are discovered in the new system, the
system is simply turned off and fi xed and then the conversion process starts again. Th e problem
with this approach is the added expense of operating two systems that perform the same function.

## Designing Tests
Understand different types of tests and when to use
### 1. Unit tests
Focus on a single unit – the class
- Black-box Testing
- White-box Testing

### 2. Integration tests
How a set of classes work together

Classes pass unit tests first
- Interface testing
- Use-Case Testing
- Interaction Testing
- System Interface Testing

### 3. System tests
- Requirements
- Usability 
- Security
- Performance
- Documentation

### 4. Acceptance tests
**Alpha**

Conducted by users to ensure they accept the system

**Beta**

Users use real data, not test data


## CHANGE MANAGEMENT
Change management is aimed at helping system users to adopt the new system and use it productively.

## Understanding Resistance to Change
What is good for the organization, is not necessarily good for the individuals who work there
Cost versus benefit of transition as well as of to-be system Adapting to new work processes requires effort, for which there may be no additional compensation.

**Training**
-	Every new system requires new skills
-	New skills may involve use of the technology itself
-	New skills may be needed to handle the changed business processes

