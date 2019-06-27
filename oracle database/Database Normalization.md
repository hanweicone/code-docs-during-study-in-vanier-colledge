[![Hide](//upload.wikimedia.org/wikipedia/foundation/2/20/CloseWindow19x19.png)](# "Hide")

[![WLE Austria Logo (no text).svg](//upload.wikimedia.org/wikipedia/commons/thumb/8/85/WLE_Austria_Logo_%28no_text%29.svg/50px-WLE_Austria_Logo_%28no_text%29.svg.png)](https://ca.wikimedia.org/wiki/Wiki_Loves_Earth/Home)

[Wiki Loves Earth: An international photographic contest where you can showcase Canada’s unique natural environment, help Wikipedia, and potentially win a prize. Everybody can participate!](https://ca.wikimedia.org/wiki/Wiki_Loves_Earth/Home)

First normal form
=================

From Wikipedia, the free encyclopedia

[Jump to navigation](#mw-head) [Jump to search](#p-search)

**First normal form** (**1NF**) is a property of a [relation](/wiki/Relation_(database) "Relation (database)") in a [relational database](/wiki/Relational_database "Relational database"). A relation is in first normal form if and only if the [domain](/wiki/Data_domain "Data domain") of each [attribute](/wiki/Column_(database) "Column (database)") contains only [atomic](#Atomicity) (indivisible) values, and the value of each attribute contains only a single value from that domain.[\[1\]](#cite_note-1) The first definition of the term, in a 1971 conference paper by [Edgar Codd](/wiki/Edgar_F._Codd "Edgar F. Codd"), defined a relation to be in first normal form when none of its domains have any sets as elements.[\[2\]](#cite_note-2)

First normal form is an essential property of a relation in a relational database. [Database normalization](/wiki/Database_normalization "Database normalization") is the process of representing a database in terms of relations in standard normal forms, where first normal is a minimal requirement.

First normal form enforces these criteria:\[_[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_\]

*   Eliminate repeating groups\[_[clarification needed](/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")_\] in individual tables
*   Create a separate table for each set of related data\[_[definition needed](/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")_\]
*   Identify each set of related data with a [primary key](/wiki/Primary_key "Primary key")

Contents
--------

*   [1 Examples](#Examples)
    *   [1.1 Designs that violate 1NF](#Designs_that_violate_1NF)
    *   [1.2 Designs that comply with 1NF](#Designs_that_comply_with_1NF)
*   [2 Atomicity](#Atomicity)
*   [3 1NF tables as representations of relations](#1NF_tables_as_representations_of_relations)
*   [4 See also](#See_also)
*   [5 References](#References)
*   [6 Further reading](#Further_reading)

Examples\[[edit](/w/index.php?title=First_normal_form&action=edit&section=1 "Edit section: Examples")\]
-------------------------------------------------------------------------------------------------------

the following scenarios first illustrate how a database design might violate first normal form, followed by examples that comply.[\[3\]](#cite_note-3)[\[4\]](#cite_note-4)

### Designs that violate 1NF\[[edit](/w/index.php?title=First_normal_form&action=edit&section=2 "Edit section: Designs that violate 1NF")\]

Below is a table that stores the names and telephone numbers of customers. One requirement though is to retain _multiple_ telephone numbers for some customers. The simplest way of satisfying this requirement is to allow the "Telephone Number" column in any given row to contain more than one value:

Customer

Customer ID

First Name

Surname

Telephone Number

123

Pooja

Singh

555-861-2025, 192-122-1111

456

San

Zhang

(555) 403-1659 Ext. 53; 182-929-2929

789

John

Doe

555-808-9633

Note that the telephone number column simply contains text: numbers of different formats, and more importantly, more than one number for two of the customers. We are duplicating related information in the same column. If we would be satisfied with such arbitrary text, we would be fine. But it's not arbitrary text at all: we obviously intended this column to contain telephone number(s). Seen as telephone numbers, the text is not _atomic_: it can be subdivided. As well, when seen as telephone numbers, the text contains more than one number in two of our rows. This representation of telephone numbers is not in first normal form: our columns contain non-atomic values, and they contain more than one of them.

An apparent solution is to introduce more columns:

Customer

Customer ID

First Name

Surname

Telephone Number1

Telephone Number2

123

Pooja

Singh

555-861-2025

192-122-1111

456

San

Zhang

(555) 403-1659 Ext. 53

182-929-2929

789

John

Doe

555-808-9633

Technically, this table does not violate the requirement for values to be atomic. However, informally, the two telephone number columns still form a "repeating group": they repeat what is conceptually the same attribute, namely a telephone number. An arbitrary and hence meaningless ordering has been introduced: why is 555-861-2025 put into the Telephone Number1 column rather than the Telephone Number2 column? There's no reason why customers could not have more than two telephone numbers, so how many Telephone Number_N_ columns should there be? It is not possible to search for a telephone number without searching an arbitrary number of columns. Adding an extra telephone number may require the table to be reorganized by the addition of a new column rather than just having a new row (tuple) added. (The null value for Telephone Number2 for customer 789 is also an issue.)

### Designs that comply with 1NF\[[edit](/w/index.php?title=First_normal_form&action=edit&section=3 "Edit section: Designs that comply with 1NF")\]

To bring the model into the first normal form, we split the strings we used to hold our telephone number information into "atomic" (i.e. indivisible) entities: single phone numbers. And we ensure no row contains more than one phone number.

Customer

Customer ID

First Name

Surname

Telephone Number

123

Pooja

Singh

555-861-2025

123

Pooja

Singh

192-122-1111

456

San

Zhang

182-929-2929

456

San

Zhang

(555) 403-1659 Ext. 53

789

John

Doe

555-808-9633

Note that the "ID" is no longer unique in this solution with duplicated customers. To uniquely identify a row, we need to use a combination of (ID, Telephone Number). The value of the combination is unique although each column separately contains repeated values. Being able to uniquely identify a row (tuple) is a requirement of 1NF.

An alternative design uses two tables:

Customer Name

Customer ID

First Name

Surname

123

Pooja

Singh

456

San

Zhang

789

John

Doe

Customer Telephone Number

Id

Customer ID

Telephone Number

1

123

555-861-2025

2

123

192-122-1111

3

456

(555) 403-1659 Ext. 53

4

456

182-929-2929

5

789

555-808-9633

Columns do not contain more than one telephone number in this design. Instead, each Customer-to-Telephone Number link appears on its own row. Using **Customer ID** as key, a _one-to-many_ relationship exists between the name and the number tables. A row in the "parent" table, **Customer Name**, can be associated with many telephone number rows in the "child" table, **Customer Telephone Number**, but each telephone number belongs to one, and only one customer.[\[5\]](#cite_note-5) It is worth noting that this design meets the additional requirements for [second](/wiki/Second_normal_form "Second normal form") and [third normal form](/wiki/Third_normal_form "Third normal form").

Atomicity\[[edit](/w/index.php?title=First_normal_form&action=edit&section=4 "Edit section: Atomicity")\]
---------------------------------------------------------------------------------------------------------

[Edgar F. Codd](/wiki/Edgar_F._Codd "Edgar F. Codd")'s definition of 1NF makes reference to the concept of 'atomicity'. Codd states that the "values in the domains on which each relation is defined are required to be atomic with respect to the [DBMS](/wiki/DBMS "DBMS")."[\[6\]](#cite_note-CoddAtmReq-6) Codd defines an atomic value as one that "cannot be decomposed into smaller pieces by the DBMS (excluding certain special functions)"[\[7\]](#cite_note-CoddAtmDefn-7) meaning a column should not be divided into parts with more than one kind of data in it such that what one part means to the DBMS depends on another part of the same column.

[Hugh Darwen](/wiki/Hugh_Darwen "Hugh Darwen") and [Chris Date](/wiki/Chris_Date "Chris Date") have suggested that Codd's concept of an "atomic value" is ambiguous, and that this ambiguity has led to widespread confusion about how 1NF should be understood.[\[8\]](#cite_note-Darwen-8)[\[9\]](#cite_note-DateConf-9) In particular, the notion of a "value that cannot be decomposed" is problematic, as it would seem to imply that few, if any, data types are atomic:

*   A character string would seem not to be atomic, as the RDBMS typically provides operators to decompose it into substrings.
*   A fixed-point number would seem not to be atomic, as the RDBMS typically provides operators to decompose it into integer and fractional components.
*   An [ISBN](/wiki/ISBN "ISBN") would seem not to be atomic, as it includes language and publisher identifier.

Date suggests that "the notion of atomicity _has no absolute meaning_":[\[10\]](#cite_note-DateNoAtm-10)[\[11\]](#cite_note-Date2015-11) a value may be considered atomic for some purposes, but may be considered an assemblage of more basic elements for other purposes. If this position is accepted, 1NF cannot be defined with reference to atomicity. Columns of any conceivable data type (from string types and numeric types to [array](/wiki/Array_data_structure "Array data structure") types and table types) are then acceptable in a 1NF table—although perhaps not always desirable; for example, it would be more desirable to separate a Customer Name column into two separate columns as First Name, Surname.

1NF tables as representations of relations\[[edit](/w/index.php?title=First_normal_form&action=edit&section=5 "Edit section: 1NF tables as representations of relations")\]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

According to Date's definition, a table is in first normal form if and only if it is "[isomorphic](/wiki/Isomorphism "Isomorphism") to some relation", which means, specifically, that it satisfies the following five conditions:[\[12\]](#cite_note-Date5Cr-12)

.mw-parser-output .templatequote{overflow:hidden;margin:1em 0;padding:0 40px}.mw-parser-output .templatequote .templatequotecite{line-height:1.5em;text-align:left;padding-left:1.6em;margin-top:0}

> 1.  There's no top-to-bottom ordering to the rows.
> 2.  There's no left-to-right ordering to the columns.
> 3.  There are no duplicate rows.
> 4.  Every row-and-column intersection contains exactly one value from the applicable domain (and nothing else).
> 5.  All columns are regular \[i.e. rows have no hidden components such as row IDs, object IDs, or hidden timestamps\].

Violation of any of these conditions would mean that the table is not strictly relational, and therefore that it is not in first normal form.

Examples of tables (or [views](/wiki/View_(database) "View (database)")) that would not meet this definition of first normal form are:

*   A table that lacks a unique key constraint. Such a table would be able to accommodate duplicate rows, in violation of condition 3.
*   A view whose definition mandates that results be returned in a particular order, so that the row-ordering is an intrinsic and meaningful aspect of the view.[\[13\]](#cite_note-ViewOrder-13) This violates condition 1. The [tuples](/wiki/Tuple "Tuple") in true relations are not ordered with respect to each other.
*   A table with at least one [nullable](/wiki/Null_(SQL) "Null (SQL)") attribute. A nullable attribute would be in violation of condition 4, which requires every column to contain exactly one value from its column's domain. It should be noted, however, that this aspect of condition 4 is controversial. It marks an important departure from [Codd](/wiki/Edgar_F._Codd "Edgar F. Codd")'s later vision of the [relational model](/wiki/Relational_model "Relational model"),[\[14\]](#cite_note-DateNullsLater-14) which made explicit provision for nulls.[\[15\]](#cite_note-CoddRule-15)

First normal form, as defined by Chris Date, permits relation-valued attributes (tables within tables). Date argues that relation-valued attributes, by means of which a column within a table can contain a table, are useful in rare cases.[\[16\]](#cite_note-DateRVA-16)

See also\[[edit](/w/index.php?title=First_normal_form&action=edit&section=6 "Edit section: See also")\]
-------------------------------------------------------------------------------------------------------

For other normal forms, see the navigation bar at the bottom of the page.

References\[[edit](/w/index.php?title=First_normal_form&action=edit&section=7 "Edit section: References")\]
-----------------------------------------------------------------------------------------------------------

1.  **[^](#cite_ref-1 "Jump up")** Elmasri, Ramez; Navathe, Shamkant B. (July 2003). _Fundamentals of Database Systems, Fourth Edition_. Pearson. p. 315. [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [0321204484](/wiki/Special:BookSources/0321204484 "Special:BookSources/0321204484"). It states that the domain of an attribute must include only _atomic_ (simple, indivisible) _values_ and that the value of any attribute in a tuple must be a _single value_ from the domain of that attribute..mw-parser-output cite.citation{font-style:inherit}.mw-parser-output .citation q{quotes:"\\"""\\"""'""'"}.mw-parser-output .citation .cs1-lock-free a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/6/65/Lock-green.svg/9px-Lock-green.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .citation .cs1-lock-limited a,.mw-parser-output .citation .cs1-lock-registration a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Lock-gray-alt-2.svg/9px-Lock-gray-alt-2.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .citation .cs1-lock-subscription a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lock-red-alt-2.svg/9px-Lock-red-alt-2.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration{color:#555}.mw-parser-output .cs1-subscription span,.mw-parser-output .cs1-registration span{border-bottom:1px dotted;cursor:help}.mw-parser-output .cs1-ws-icon a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/12px-Wikisource-logo.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output code.cs1-code{color:inherit;background:inherit;border:inherit;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;font-size:100%}.mw-parser-output .cs1-visible-error{font-size:100%}.mw-parser-output .cs1-maint{display:none;color:#33aa33;margin-left:0.3em}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration,.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left,.mw-parser-output .cs1-kern-wl-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right,.mw-parser-output .cs1-kern-wl-right{padding-right:0.2em}
2.  **[^](#cite_ref-2 "Jump up")** E. F. Codd (Oct 1972), _Further normalization of the database relational model_, Courant Institute: Prentice-Hall, [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [013196741X](/wiki/Special:BookSources/013196741X "Special:BookSources/013196741X"), A relation is in _first normal form_ if it has the property that none of its domains has elements which are themselves sets.
3.  **[^](#cite_ref-3 "Jump up")** [studytonight.com](http://www.studytonight.com/dbms/database-normalization.php)
4.  **[^](#cite_ref-4 "Jump up")** [stackoverflow.com](https://stackoverflow.com/questions/723998/can-someone-please-give-an-example-of-1nf-2nf-and-3nf-in-plain-english)
5.  **[^](#cite_ref-5 "Jump up")** In the "real" world, that would not be a good assumption.
6.  **[^](#cite_ref-CoddAtmReq_6-0 "Jump up")** Codd, E. F. _The Relational Model for Database Management Version 2_ (Addison-Wesley, 1990).
7.  **[^](#cite_ref-CoddAtmDefn_7-0 "Jump up")** Codd, E. F. _The Relational Model for Database Management Version 2_ (Addison-Wesley, 1990), p. 6.
8.  **[^](#cite_ref-Darwen_8-0 "Jump up")** Darwen, Hugh. "Relation-Valued Attributes; or, Will the Real First Normal Form Please Stand Up?", in C. J. Date and Hugh Darwen, _Relational Database Writings 1989-1991_ (Addison-Wesley, 1992).
9.  **[^](#cite_ref-DateConf_9-0 "Jump up")** "\[F\]or many years," writes Date, "I was as confused as anyone else. What's worse, I did my best (worst?) to spread that confusion through my writings, seminars, and other presentations." Date, C. J. \["What First Normal Form Really Means"\] in _Date on Database: Writings 2000-2006_ (Springer-Verlag, 2006), p. 108
10.  **[^](#cite_ref-DateNoAtm_10-0 "Jump up")** Date, C. J. \["What First Normal Form Really Means"\] p. 112.
11.  **[^](#cite_ref-Date2015_11-0 "Jump up")** C.J. Date (6 November 2015). [_SQL and Relational Theory: How to Write Accurate SQL Code_](https://books.google.com/books?id=BCjkCgAAQBAJ&pg=PA50). "O'Reilly Media, Inc.". pp. 50–. [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [978-1-4919-4115-7](/wiki/Special:BookSources/978-1-4919-4115-7 "Special:BookSources/978-1-4919-4115-7"). Retrieved 31 October 2018.
12.  **[^](#cite_ref-Date5Cr_12-0 "Jump up")** Date, C. J. \["What First Normal Form Really Means"\] pp. 127–128.
13.  **[^](#cite_ref-ViewOrder_13-0 "Jump up")** Such views cannot be created using [SQL](/wiki/SQL "SQL") that conforms to the [SQL:2003](/wiki/SQL:2003 "SQL:2003") standard.
14.  **[^](#cite_ref-DateNullsLater_14-0 "Jump up")** "Codd first defined the relational model in 1969 and didn't introduce nulls until 1979" Date, C. J. _SQL and Relational Theory_ (O'Reilly, 2009), Appendix A.2.
15.  **[^](#cite_ref-CoddRule_15-0 "Jump up")** The third of Codd's 12 rules states that "Null values ... \[must be\] supported in a fully relational DBMS for representing missing information and inapplicable information in a systematic way, independent of data type." Codd, E. F. "Is Your DBMS Really Relational?" _Computerworld_, October 14, 1985.
16.  **[^](#cite_ref-DateRVA_16-0 "Jump up")** Date, C. J. \["What First Normal Form Really Means"\] pp. 121–126.

Further reading\[[edit](/w/index.php?title=First_normal_form&action=edit&section=8 "Edit section: Further reading")\]
---------------------------------------------------------------------------------------------------------------------

.mw-parser-output .refbegin{font-size:90%;margin-bottom:0.5em}.mw-parser-output .refbegin-hanging-indents>ul{list-style-type:none;margin-left:0}.mw-parser-output .refbegin-hanging-indents>ul>li,.mw-parser-output .refbegin-hanging-indents>dl>dd{margin-left:0;padding-left:3.2em;text-indent:-3.2em;list-style:none}.mw-parser-output .refbegin-100{font-size:100%}

*   Date, C. J., & Lorentzos, N., & Darwen, H. (2002). _[Temporal Data & the Relational Model](http://www.elsevier.com/wps/product/cws_home/680662)\[_[permanent dead link](/wiki/Wikipedia:Link_rot "Wikipedia:Link rot")_\]_ (1st ed.). Morgan Kaufmann. [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [1-55860-855-9](/wiki/Special:BookSources/1-55860-855-9 "Special:BookSources/1-55860-855-9").
*   Date, C. J. (1999), _[An Introduction to Database Systems](https://web.archive.org/web/20050404010227/http://www.aw-bc.com/catalog/academic/product/0,1144,0321197844,00.html)_ (8th ed.). Addison-Wesley Longman. [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [0-321-19784-4](/wiki/Special:BookSources/0-321-19784-4 "Special:BookSources/0-321-19784-4").
*   Kent, W. (1983) _[A Simple Guide to Five Normal Forms in Relational Database Theory](http://www.bkent.net/Doc/simple5.htm)_, Communications of the ACM, vol. 26, pp. 120–125

*   Codd, E.F. (1970). A Relational Model of Data for. Large Shared Data Banks. IBM Research Laboratory, San Jose, California.
*   Codd, E. F. (1971). Further Normalization of the Relational Model. Courant Computer Science Symposium 6 in Data Base Systems edited by Rustin, R.

hide

*   [v](/wiki/Template:Database_normalization "Template:Database normalization")
*   [t](/wiki/Template_talk:Database_normalization "Template talk:Database normalization")
*   [e](//en.wikipedia.org/w/index.php?title=Template:Database_normalization&action=edit)

[Database normalization](/wiki/Database_normalization "Database normalization")

*   [Unnormalized form](/wiki/Unnormalized_form "Unnormalized form") (UNF/NF2)
*   First normal form (1NF)
*   [Second normal form](/wiki/Second_normal_form "Second normal form") (2NF)
*   [Third normal form](/wiki/Third_normal_form "Third normal form") (3NF)
*   [Elementary key normal form](/wiki/Elementary_key_normal_form "Elementary key normal form") (EKNF)
*   [Boyce–Codd normal form](/wiki/Boyce%E2%80%93Codd_normal_form "Boyce–Codd normal form") (3.5NF / BCNF)
*   [Fourth normal form](/wiki/Fourth_normal_form "Fourth normal form") (4NF)
*   [Fifth normal form](/wiki/Fifth_normal_form "Fifth normal form") (5NF / PJNF)
*   [Domain-key normal form](/wiki/Domain-key_normal_form "Domain-key normal form") (DKNF)
*   [Sixth normal form](/wiki/Sixth_normal_form "Sixth normal form") (6NF)

[Denormalization](/wiki/Denormalization "Denormalization")

![](//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)

Retrieved from "[https://en.wikipedia.org/w/index.php?title=First\_normal\_form&oldid=895027109](https://en.wikipedia.org/w/index.php?title=First_normal_form&oldid=895027109)"

[Categories](/wiki/Help:Category "Help:Category"):

*   [Database normalization](/wiki/Category:Database_normalization "Category:Database normalization")

Hidden categories:

*   [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
*   [Articles with unsourced statements from October 2018](/wiki/Category:Articles_with_unsourced_statements_from_October_2018 "Category:Articles with unsourced statements from October 2018")
*   [Wikipedia articles needing clarification from October 2018](/wiki/Category:Wikipedia_articles_needing_clarification_from_October_2018 "Category:Wikipedia articles needing clarification from October 2018")
*   [All articles with dead external links](/wiki/Category:All_articles_with_dead_external_links "Category:All articles with dead external links")
*   [Articles with dead external links from October 2017](/wiki/Category:Articles_with_dead_external_links_from_October_2017 "Category:Articles with dead external links from October 2017")
*   [Articles with permanently dead external links](/wiki/Category:Articles_with_permanently_dead_external_links "Category:Articles with permanently dead external links")
