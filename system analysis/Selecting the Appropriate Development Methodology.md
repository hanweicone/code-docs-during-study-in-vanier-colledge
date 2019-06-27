# Selecting the Appropriate Development Methodology

## Figure 2.6
| Usefulness in  Developing Systems  | Waterfall |  Parallel | V-Model | Iterative | System Prototyping | Throwaway Prototyping| Agile Development |
|:---------------------------------: |:---------:|:---------:|:-------:|:---------:|:------------------:|:--------------------:|:-----------------:|
| with unclear user requirements| Poor | Poor | Poor | Good | Excellent | Excellent | Excellent |
| with unfamiliar technology | Poor | Poor | Poor | Good | Poor | Excellent | Poor |
| that are complex | Good | Good | Good | Good | Poor | Excellent | Poor |
| that are reliable  | Good | Good | Excellent | Good | Poor | Excellent | Good |
| with short time schedule | Poor | Good | Poor | Excellent | Excellent | Good | Excellent |
| with schedule visibility | Poor | Poor | Poor | Excellent | Excellent | Good | Good |

There are many methodologies. The first challenge
faced by project managers is to select which methodology to use. Choosing a
methodology is not simple, because no one methodology is always best. (If it were,
we’d simply use it everywhere!) Many organizations have standards and policies to
guide the choice of methodology. You will find that organizations range from having
one “approved” methodology to having several methodology options to having
no formal policies at all.

Figure 2.6 summarizes some important methodology selection criteria. One
important item not discussed in this figure is the degree of experience of the analyst
team. Many of the RAD and agile development methodologies require the use of new
tools and techniques that have a significant learning curve. Often, these tools and techniques
increase the complexity of the project and require extra time for learning. Once
they are adopted and the team becomes experienced, the tools and techniques can significantly
increase the speed in which the methodology can deliver a final system.

## Clarity of User Requirements 
When the user requirements for what the system
should do are unclear, it is difficult to understand them by talking about them and
explaining them with written reports. Users normally need to interact with technology
to really understand what the new system can do and how to best apply it to
their needs. System prototyping and throwaway prototyping are usually more
appropriate when user requirements are unclear, because they provide prototypes
for users to interact with early in the SDLC. Agile development may also be appropriate
if on-site user input is available.

## Familiarity with Technology
When the system will use new technology with which
the analysts and programmers are not familiar (e.g., the first Web development project
with Ajax), applying the new technology early in the methodology will improve
the chance of success. If the system is designed without some familiarity with the
base technology, risks increase because the tools may not be capable of doing what
is needed. Throwaway prototyping is particularly appropriate for situations where
there is a lack of familiarity with technology, because it explicitly encourages the
developers to create design prototypes for areas with high risks. Iterative development
is good as well, because opportunities are created to investigate the technology
in some depth before the design is complete. While one might think that system
prototyping would also be appropriate, it is much less so because the early prototypes
that are built usually only scratch the surface of the new technology. Typically,
it is only after several prototypes and several months that the developers discover
weaknesses or problems in the new technology.

## System Complexity
Complex systems require careful and detailed analysis and
design. Throwaway prototyping is particularly well suited to such detailed analysis
and design, but system prototyping is not. The waterfall methodologies can handle
complex systems, but without the ability to get the system or prototypes into users’
hands early on, some key issues may be overlooked. Although iterative development
methodologies enable users to interact with the system early in the process,
we have observed that project teams who follow these methodologies tend to devote
less attention to the analysis of the complete problem domain than they might if
they were using other methodologies.

## System Reliability 
System reliability is usually an important factor in system
development. After all, who wants an unreliable system? However, reliability is just
one factor among several. For some applications, reliability is truly critical (e.g.,
medical equipment, missile control systems), while for other applications it is
merely important (e.g., games, Internet video). The V-model is useful when reliability
is important, due to its emphasis on testing. Throwaway prototyping is most
appropriate when system reliability is a high priority, because detailed analysis and
design phases are combined with the ability for the project team to test many different
approaches through design prototypes before completing the design. System
prototyping is generally not a good choice when reliability is critical, due to the
lack of careful analysis and design phases that are essential to dependable systems.
## Short Time Schedules 
Projects that have short time schedules are well suited for
RAD methodologies because those methodologies are designed to increase the
speed of development. Iterative development and system prototyping are excellent
choices when time lines are short because they best enable the project team to
adjust the functionality in the system on the basis of a specific delivery date. If the
project schedule starts to slip, it can be readjusted by removal of the functionality
from the version or prototype under development. Waterfall-based methodologies
are the worst choice when time is at a premium, because they do not allow for easy
schedule changes.
## Schedule Visibility 
One of the greatest challenges in systems development is knowing
whether a project is on schedule. This is particularly true of the waterfall-based
methodologies because design and implementation occur at the end of the project.
The RAD methodologies move many of the critical design decisions to a position
earlier in the project to help project.
