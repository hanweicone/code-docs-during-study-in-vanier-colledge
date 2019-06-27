<div id="bodyContent" class="mw-body-content">

<div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>

[Jump to navigation](#mw-head) [Jump to search](#p-search)

<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr">

<div class="mw-parser-output">

**First normal form** (**1NF**) is a property of a [relation](/wiki/Relation_(database) "Relation (database)") in a [relational database](/wiki/Relational_database "Relational database"). A relation is in first normal form if and only if the [domain](/wiki/Data_domain "Data domain") of each [attribute](/wiki/Column_(database) "Column (database)") contains only [atomic](#Atomicity) (indivisible) values, and the value of each attribute contains only a single value from that domain.<sup id="cite_ref-1" class="reference">[[1]](#cite_note-1)</sup> The first definition of the term, in a 1971 conference paper by [Edgar Codd](/wiki/Edgar_F._Codd "Edgar F. Codd"), defined a relation to be in first normal form when none of its domains have any sets as elements.<sup id="cite_ref-2" class="reference">[[2]](#cite_note-2)</sup>

First normal form is an essential property of a relation in a relational database. [Database normalization](/wiki/Database_normalization "Database normalization") is the process of representing a database in terms of relations in standard normal forms, where first normal is a minimal requirement.

First normal form enforces these criteria:<sup class="noprint Inline-Template Template-Fact" style="white-space:nowrap;">[_[<span title="This claim needs references to reliable sources. (October 2018)">citation needed</span>](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_]</sup>

*   Eliminate repeating groups<sup class="noprint Inline-Template" style="margin-left:0.1em; white-space:nowrap;">[_[<span title="The text near this tag may need clarification or removal of jargon. (October 2018)">clarification needed</span>](/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")_]</sup> in individual tables
*   Create a separate table for each set of related data<sup class="noprint Inline-Template" style="white-space:nowrap;">[_[<span title="You can help -- (October 2018)">definition needed</span>](/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")_]</sup>
*   Identify each set of related data with a [primary key](/wiki/Primary_key "Primary key")

<div id="toc" class="toc"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none">

<div class="toctitle" lang="en" dir="ltr">

## Contents

<span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>

*   [<span class="tocnumber">1</span> <span class="toctext">Examples</span>](#Examples)
    *   [<span class="tocnumber">1.1</span> <span class="toctext">Designs that violate 1NF</span>](#Designs_that_violate_1NF)
    *   [<span class="tocnumber">1.2</span> <span class="toctext">Designs that comply with 1NF</span>](#Designs_that_comply_with_1NF)
*   [<span class="tocnumber">2</span> <span class="toctext">Atomicity</span>](#Atomicity)
*   [<span class="tocnumber">3</span> <span class="toctext">1NF tables as representations of relations</span>](#1NF_tables_as_representations_of_relations)
*   [<span class="tocnumber">4</span> <span class="toctext">See also</span>](#See_also)
*   [<span class="tocnumber">5</span> <span class="toctext">References</span>](#References)
*   [<span class="tocnumber">6</span> <span class="toctext">Further reading</span>](#Further_reading)

</div>

## <span class="mw-headline" id="Examples">Examples</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=1 "Edit section: Examples")<span class="mw-editsection-bracket">]</span></span>

the following scenarios first illustrate how a database design might violate first normal form, followed by examples that comply.<sup id="cite_ref-3" class="reference">[[3]](#cite_note-3)</sup><sup id="cite_ref-4" class="reference">[[4]](#cite_note-4)</sup>

### <span class="mw-headline" id="Designs_that_violate_1NF">Designs that violate 1NF</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=2 "Edit section: Designs that violate 1NF")<span class="mw-editsection-bracket">]</span></span>

Below is a table that stores the names and telephone numbers of customers. One requirement though is to retain _multiple_ telephone numbers for some customers. The simplest way of satisfying this requirement is to allow the "Telephone Number" column in any given row to contain more than one value:

<table class="wikitable customer"><caption>Customer</caption>

<tbody>

<tr>

<th>Customer ID</th>

<th>First Name</th>

<th>Surname</th>

<th>Telephone Number</th>

</tr>

<tr>

<td>123</td>

<td>Pooja</td>

<td>Singh</td>

<td>555-861-2025, 192-122-1111</td>

</tr>

<tr>

<td>456</td>

<td>San</td>

<td>Zhang</td>

<td>(555) 403-1659 Ext. 53; 182-929-2929</td>

</tr>

<tr>

<td>789</td>

<td>John</td>

<td>Doe</td>

<td>555-808-9633</td>

</tr>

</tbody>

</table>

Note that the telephone number column simply contains text: numbers of different formats, and more importantly, more than one number for two of the customers. We are duplicating related information in the same column. If we would be satisfied with such arbitrary text, we would be fine. But it's not arbitrary text at all: we obviously intended this column to contain telephone number(s). Seen as telephone numbers, the text is not _atomic_: it can be subdivided. As well, when seen as telephone numbers, the text contains more than one number in two of our rows. This representation of telephone numbers is not in first normal form: our columns contain non-atomic values, and they contain more than one of them.

An apparent solution is to introduce more columns:

<table class="wikitable customer"><caption>Customer</caption>

<tbody>

<tr>

<th>Customer ID</th>

<th>First Name</th>

<th>Surname</th>

<th>Telephone Number1</th>

<th>Telephone Number2</th>

</tr>

<tr>

<td>123</td>

<td>Pooja</td>

<td>Singh</td>

<td>555-861-2025</td>

<td>192-122-1111</td>

</tr>

<tr>

<td>456</td>

<td>San</td>

<td>Zhang</td>

<td>(555) 403-1659 Ext. 53</td>

<td>182-929-2929</td>

</tr>

<tr>

<td>789</td>

<td>John</td>

<td>Doe</td>

<td>555-808-9633</td>

<td></td>

</tr>

</tbody>

</table>

Technically, this table does not violate the requirement for values to be atomic. However, informally, the two telephone number columns still form a "repeating group": they repeat what is conceptually the same attribute, namely a telephone number. An arbitrary and hence meaningless ordering has been introduced: why is 555-861-2025 put into the Telephone Number1 column rather than the Telephone Number2 column? There's no reason why customers could not have more than two telephone numbers, so how many Telephone Number_N_ columns should there be? It is not possible to search for a telephone number without searching an arbitrary number of columns. Adding an extra telephone number may require the table to be reorganized by the addition of a new column rather than just having a new row (tuple) added. (The null value for Telephone Number2 for customer 789 is also an issue.)

### <span class="mw-headline" id="Designs_that_comply_with_1NF">Designs that comply with 1NF</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=3 "Edit section: Designs that comply with 1NF")<span class="mw-editsection-bracket">]</span></span>

To bring the model into the first normal form, we split the strings we used to hold our telephone number information into "atomic" (i.e. indivisible) entities: single phone numbers. And we ensure no row contains more than one phone number.

<table class="wikitable customer"><caption>Customer</caption>

<tbody>

<tr>

<th>Customer ID</th>

<th>First Name</th>

<th>Surname</th>

<th>Telephone Number</th>

</tr>

<tr>

<td>123</td>

<td>Pooja</td>

<td>Singh</td>

<td>555-861-2025</td>

</tr>

<tr>

<td>123</td>

<td>Pooja</td>

<td>Singh</td>

<td>192-122-1111</td>

</tr>

<tr>

<td>456</td>

<td>San</td>

<td>Zhang</td>

<td>182-929-2929</td>

</tr>

<tr>

<td>456</td>

<td>San</td>

<td>Zhang</td>

<td>(555) 403-1659 Ext. 53</td>

</tr>

<tr>

<td>789</td>

<td>John</td>

<td>Doe</td>

<td>555-808-9633</td>

</tr>

</tbody>

</table>

Note that the "ID" is no longer unique in this solution with duplicated customers. To uniquely identify a row, we need to use a combination of (ID, Telephone Number). The value of the combination is unique although each column separately contains repeated values. Being able to uniquely identify a row (tuple) is a requirement of 1NF.

An alternative design uses two tables:

<table>

<tbody>

<tr>

<td valign="top">

<table class="wikitable"><caption>Customer Name</caption>

<tbody>

<tr>

<th><u>Customer ID</u></th>

<th>First Name</th>

<th>Surname</th>

</tr>

<tr>

<td>123</td>

<td>Pooja</td>

<td>Singh</td>

</tr>

<tr>

<td>456</td>

<td>San</td>

<td>Zhang</td>

</tr>

<tr>

<td>789</td>

<td>John</td>

<td>Doe</td>

</tr>

</tbody>

</table>

</td>

<td valign="top">

<table class="wikitable"><caption>Customer Telephone Number</caption>

<tbody>

<tr>

<th>Id</th>

<th>Customer ID</th>

<th><u>Telephone Number</u></th>

</tr>

<tr>

<td>1</td>

<td>123</td>

<td>555-861-2025</td>

</tr>

<tr>

<td>2</td>

<td>123</td>

<td>192-122-1111</td>

</tr>

<tr>

<td>3</td>

<td>456</td>

<td>(555) 403-1659 Ext. 53</td>

</tr>

<tr>

<td>4</td>

<td>456</td>

<td>182-929-2929</td>

</tr>

<tr>

<td>5</td>

<td>789</td>

<td>555-808-9633</td>

</tr>

</tbody>

</table>

</td>

</tr>

</tbody>

</table>

Columns do not contain more than one telephone number in this design. Instead, each Customer-to-Telephone Number link appears on its own row. Using **Customer ID** as key, a _one-to-many_ relationship exists between the name and the number tables. A row in the "parent" table, **Customer Name**, can be associated with many telephone number rows in the "child" table, **Customer Telephone Number**, but each telephone number belongs to one, and only one customer.<sup id="cite_ref-5" class="reference">[[5]](#cite_note-5)</sup> It is worth noting that this design meets the additional requirements for [second](/wiki/Second_normal_form "Second normal form") and [third normal form](/wiki/Third_normal_form "Third normal form").

## <span class="mw-headline" id="Atomicity">Atomicity</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=4 "Edit section: Atomicity")<span class="mw-editsection-bracket">]</span></span>

[Edgar F. Codd](/wiki/Edgar_F._Codd "Edgar F. Codd")'s definition of 1NF makes reference to the concept of 'atomicity'. Codd states that the "values in the domains on which each relation is defined are required to be atomic with respect to the [DBMS](/wiki/DBMS "DBMS")."<sup id="cite_ref-CoddAtmReq_6-0" class="reference">[[6]](#cite_note-CoddAtmReq-6)</sup> Codd defines an atomic value as one that "cannot be decomposed into smaller pieces by the DBMS (excluding certain special functions)"<sup id="cite_ref-CoddAtmDefn_7-0" class="reference">[[7]](#cite_note-CoddAtmDefn-7)</sup> meaning a column should not be divided into parts with more than one kind of data in it such that what one part means to the DBMS depends on another part of the same column.

[Hugh Darwen](/wiki/Hugh_Darwen "Hugh Darwen") and [Chris Date](/wiki/Chris_Date "Chris Date") have suggested that Codd's concept of an "atomic value" is ambiguous, and that this ambiguity has led to widespread confusion about how 1NF should be understood.<sup id="cite_ref-Darwen_8-0" class="reference">[[8]](#cite_note-Darwen-8)</sup><sup id="cite_ref-DateConf_9-0" class="reference">[[9]](#cite_note-DateConf-9)</sup> In particular, the notion of a "value that cannot be decomposed" is problematic, as it would seem to imply that few, if any, data types are atomic:

*   A character string would seem not to be atomic, as the RDBMS typically provides operators to decompose it into substrings.
*   A fixed-point number would seem not to be atomic, as the RDBMS typically provides operators to decompose it into integer and fractional components.
*   An [ISBN](/wiki/ISBN "ISBN") would seem not to be atomic, as it includes language and publisher identifier.

Date suggests that "the notion of atomicity _has no absolute meaning_":<sup id="cite_ref-DateNoAtm_10-0" class="reference">[[10]](#cite_note-DateNoAtm-10)</sup><sup id="cite_ref-Date2015_11-0" class="reference">[[11]](#cite_note-Date2015-11)</sup> a value may be considered atomic for some purposes, but may be considered an assemblage of more basic elements for other purposes. If this position is accepted, 1NF cannot be defined with reference to atomicity. Columns of any conceivable data type (from string types and numeric types to [array](/wiki/Array_data_structure "Array data structure") types and table types) are then acceptable in a 1NF table—although perhaps not always desirable; for example, it would be more desirable to separate a Customer Name column into two separate columns as First Name, Surname.

## <span class="mw-headline" id="1NF_tables_as_representations_of_relations">1NF tables as representations of relations</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=5 "Edit section: 1NF tables as representations of relations")<span class="mw-editsection-bracket">]</span></span>

According to Date's definition, a table is in first normal form if and only if it is "[isomorphic](/wiki/Isomorphism "Isomorphism") to some relation", which means, specifically, that it satisfies the following five conditions:<sup id="cite_ref-Date5Cr_12-0" class="reference">[[12]](#cite_note-Date5Cr-12)</sup>

<style data-mw-deduplicate="TemplateStyles:r886047036">.mw-parser-output .templatequote{overflow:hidden;margin:1em 0;padding:0 40px}.mw-parser-output .templatequote .templatequotecite{line-height:1.5em;text-align:left;padding-left:1.6em;margin-top:0}</style>

> 1.  There's no top-to-bottom ordering to the rows.
> 2.  There's no left-to-right ordering to the columns.
> 3.  There are no duplicate rows.
> 4.  Every row-and-column intersection contains exactly one value from the applicable domain (and nothing else).
> 5.  All columns are regular [i.e. rows have no hidden components such as row IDs, object IDs, or hidden timestamps].

Violation of any of these conditions would mean that the table is not strictly relational, and therefore that it is not in first normal form.

Examples of tables (or [views](/wiki/View_(database) "View (database)")) that would not meet this definition of first normal form are:

*   A table that lacks a unique key constraint. Such a table would be able to accommodate duplicate rows, in violation of condition 3.
*   A view whose definition mandates that results be returned in a particular order, so that the row-ordering is an intrinsic and meaningful aspect of the view.<sup id="cite_ref-ViewOrder_13-0" class="reference">[[13]](#cite_note-ViewOrder-13)</sup> This violates condition 1\. The [tuples](/wiki/Tuple "Tuple") in true relations are not ordered with respect to each other.
*   A table with at least one [nullable](/wiki/Null_(SQL) "Null (SQL)") attribute. A nullable attribute would be in violation of condition 4, which requires every column to contain exactly one value from its column's domain. It should be noted, however, that this aspect of condition 4 is controversial. It marks an important departure from [Codd](/wiki/Edgar_F._Codd "Edgar F. Codd")'s later vision of the [relational model](/wiki/Relational_model "Relational model"),<sup id="cite_ref-DateNullsLater_14-0" class="reference">[[14]](#cite_note-DateNullsLater-14)</sup> which made explicit provision for nulls.<sup id="cite_ref-CoddRule_15-0" class="reference">[[15]](#cite_note-CoddRule-15)</sup>

First normal form, as defined by Chris Date, permits relation-valued attributes (tables within tables). Date argues that relation-valued attributes, by means of which a column within a table can contain a table, are useful in rare cases.<sup id="cite_ref-DateRVA_16-0" class="reference">[[16]](#cite_note-DateRVA-16)</sup>

## <span class="mw-headline" id="See_also">See also</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=6 "Edit section: See also")<span class="mw-editsection-bracket">]</span></span>

<div role="note" class="hatnote navigation-not-searchable">For other normal forms, see the navigation bar at the bottom of the page.</div>

## <span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=7 "Edit section: References")<span class="mw-editsection-bracket">]</span></span>

<div class="reflist columns references-column-width" style="-moz-column-width: 30em; -webkit-column-width: 30em; column-width: 30em; list-style-type: decimal;">

1.  <span class="mw-cite-backlink">**[^](#cite_ref-1 "Jump up")**</span> <span class="reference-text"><cite class="citation book">Elmasri, Ramez; Navathe, Shamkant B. (July 2003). _Fundamentals of Database Systems, Fourth Edition_. Pearson. p. 315\. [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [<bdi>0321204484</bdi>](/wiki/Special:BookSources/0321204484 "Special:BookSources/0321204484"). <q>It states that the domain of an attribute must include only _atomic_ (simple, indivisible) _values_ and that the value of any attribute in a tuple must be a _single value_ from the domain of that attribute.</q></cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Fundamentals+of+Database+Systems%2C+Fourth+Edition&amp;rft.pages=315&amp;rft.pub=Pearson&amp;rft.date=2003-07&amp;rft.isbn=0321204484&amp;rft.au=Elmasri%2C+Ramez&amp;rft.au=Navathe%2C+Shamkant+B.&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AFirst+normal+form" class="Z3988"></span><style data-mw-deduplicate="TemplateStyles:r886058088">.mw-parser-output cite.citation{font-style:inherit}.mw-parser-output .citation q{quotes:"\"""\"""'""'"}.mw-parser-output .citation .cs1-lock-free a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/6/65/Lock-green.svg/9px-Lock-green.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .citation .cs1-lock-limited a,.mw-parser-output .citation .cs1-lock-registration a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Lock-gray-alt-2.svg/9px-Lock-gray-alt-2.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .citation .cs1-lock-subscription a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lock-red-alt-2.svg/9px-Lock-red-alt-2.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration{color:#555}.mw-parser-output .cs1-subscription span,.mw-parser-output .cs1-registration span{border-bottom:1px dotted;cursor:help}.mw-parser-output .cs1-ws-icon a{background:url("//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/12px-Wikisource-logo.svg.png")no-repeat;background-position:right .1em center}.mw-parser-output code.cs1-code{color:inherit;background:inherit;border:inherit;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;font-size:100%}.mw-parser-output .cs1-visible-error{font-size:100%}.mw-parser-output .cs1-maint{display:none;color:#33aa33;margin-left:0.3em}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration,.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left,.mw-parser-output .cs1-kern-wl-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right,.mw-parser-output .cs1-kern-wl-right{padding-right:0.2em}</style></span>
2.  <span class="mw-cite-backlink">**[^](#cite_ref-2 "Jump up")**</span> <span class="reference-text"><cite id="CITEREFE._F._Codd1972" class="citation">E. F. Codd (Oct 1972), _Further normalization of the database relational model_, Courant Institute: Prentice-Hall, [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [<bdi>013196741X</bdi>](/wiki/Special:BookSources/013196741X "Special:BookSources/013196741X"), <q>A relation is in _first normal form_ if it has the property that none of its domains has elements which are themselves sets.</q></cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Further+normalization+of+the+database+relational+model&amp;rft.place=Courant+Institute&amp;rft.pub=Prentice-Hall&amp;rft.date=1972-10&amp;rft.isbn=013196741X&amp;rft.au=E.+F.+Codd&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AFirst+normal+form" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r886058088"></span>
3.  <span class="mw-cite-backlink">**[^](#cite_ref-3 "Jump up")**</span> <span class="reference-text">[studytonight.com](http://www.studytonight.com/dbms/database-normalization.php)</span>
4.  <span class="mw-cite-backlink">**[^](#cite_ref-4 "Jump up")**</span> <span class="reference-text">[stackoverflow.com](https://stackoverflow.com/questions/723998/can-someone-please-give-an-example-of-1nf-2nf-and-3nf-in-plain-english)</span>
5.  <span class="mw-cite-backlink">**[^](#cite_ref-5 "Jump up")**</span> <span class="reference-text">In the "real" world, that would not be a good assumption.</span>
6.  <span class="mw-cite-backlink">**[^](#cite_ref-CoddAtmReq_6-0 "Jump up")**</span> <span class="reference-text">Codd, E. F. _The Relational Model for Database Management Version 2_ (Addison-Wesley, 1990).</span>
7.  <span class="mw-cite-backlink">**[^](#cite_ref-CoddAtmDefn_7-0 "Jump up")**</span> <span class="reference-text">Codd, E. F. _The Relational Model for Database Management Version 2_ (Addison-Wesley, 1990), p. 6.</span>
8.  <span class="mw-cite-backlink">**[^](#cite_ref-Darwen_8-0 "Jump up")**</span> <span class="reference-text">Darwen, Hugh. "Relation-Valued Attributes; or, Will the Real First Normal Form Please Stand Up?", in C. J. Date and Hugh Darwen, _Relational Database Writings 1989-1991_ (Addison-Wesley, 1992).</span>
9.  <span class="mw-cite-backlink">**[^](#cite_ref-DateConf_9-0 "Jump up")**</span> <span class="reference-text">"[F]or many years," writes Date, "I was as confused as anyone else. What's worse, I did my best (worst?) to spread that confusion through my writings, seminars, and other presentations." Date, C. J. ["What First Normal Form Really Means"] in _Date on Database: Writings 2000-2006_ (Springer-Verlag, 2006), p. 108</span>
10.  <span class="mw-cite-backlink">**[^](#cite_ref-DateNoAtm_10-0 "Jump up")**</span> <span class="reference-text">Date, C. J. ["What First Normal Form Really Means"] p. 112.</span>
11.  <span class="mw-cite-backlink">**[^](#cite_ref-Date2015_11-0 "Jump up")**</span> <span class="reference-text"><cite class="citation book">C.J. Date (6 November 2015). [_SQL and Relational Theory: How to Write Accurate SQL Code_](https://books.google.com/books?id=BCjkCgAAQBAJ&pg=PA50). "O'Reilly Media, Inc.". pp. 50–. [ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [<bdi>978-1-4919-4115-7</bdi>](/wiki/Special:BookSources/978-1-4919-4115-7 "Special:BookSources/978-1-4919-4115-7")<span class="reference-accessdate">. Retrieved <span class="nowrap">31 October</span> 2018</span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=SQL+and+Relational+Theory%3A+How+to+Write+Accurate+SQL+Code&amp;rft.pages=50-&amp;rft.pub=%22O%27Reilly+Media%2C+Inc.%22&amp;rft.date=2015-11-06&amp;rft.isbn=978-1-4919-4115-7&amp;rft.au=C.J.+Date&amp;rft_id=https%3A%2F%2Fbooks.google.com%2Fbooks%3Fid%3DBCjkCgAAQBAJ%26pg%3DPA50&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AFirst+normal+form" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r886058088"></span>
12.  <span class="mw-cite-backlink">**[^](#cite_ref-Date5Cr_12-0 "Jump up")**</span> <span class="reference-text">Date, C. J. ["What First Normal Form Really Means"] pp. 127–128.</span>
13.  <span class="mw-cite-backlink">**[^](#cite_ref-ViewOrder_13-0 "Jump up")**</span> <span class="reference-text">Such views cannot be created using [SQL](/wiki/SQL "SQL") that conforms to the [SQL:2003](/wiki/SQL:2003 "SQL:2003") standard.</span>
14.  <span class="mw-cite-backlink">**[^](#cite_ref-DateNullsLater_14-0 "Jump up")**</span> <span class="reference-text">"Codd first defined the relational model in 1969 and didn't introduce nulls until 1979" Date, C. J. _SQL and Relational Theory_ (O'Reilly, 2009), Appendix A.2.</span>
15.  <span class="mw-cite-backlink">**[^](#cite_ref-CoddRule_15-0 "Jump up")**</span> <span class="reference-text">The third of Codd's 12 rules states that "Null values ... [must be] supported in a fully relational DBMS for representing missing information and inapplicable information in a systematic way, independent of data type." Codd, E. F. "Is Your DBMS Really Relational?" _Computerworld_, October 14, 1985.</span>
16.  <span class="mw-cite-backlink">**[^](#cite_ref-DateRVA_16-0 "Jump up")**</span> <span class="reference-text">Date, C. J. ["What First Normal Form Really Means"] pp. 121–126.</span>

</div>

## <span class="mw-headline" id="Further_reading">Further reading</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span>[edit](/w/index.php?title=First_normal_form&action=edit&section=8 "Edit section: Further reading")<span class="mw-editsection-bracket">]</span></span>

<style data-mw-deduplicate="TemplateStyles:r886047268">.mw-parser-output .refbegin{font-size:90%;margin-bottom:0.5em}.mw-parser-output .refbegin-hanging-indents>ul{list-style-type:none;margin-left:0}.mw-parser-output .refbegin-hanging-indents>ul>li,.mw-parser-output .refbegin-hanging-indents>dl>dd{margin-left:0;padding-left:3.2em;text-indent:-3.2em;list-style:none}.mw-parser-output .refbegin-100{font-size:100%}</style>

<div class="refbegin" style="">

*   Date, C. J., & Lorentzos, N., & Darwen, H. (2002). _[Temporal Data & the Relational Model](http://www.elsevier.com/wps/product/cws_home/680662)<sup class="noprint Inline-Template"><span style="white-space: nowrap;">[_[<span title="&nbsp;Dead link since October 2017">permanent dead link</span>](/wiki/Wikipedia:Link_rot "Wikipedia:Link rot")_]</span></sup>_ (1st ed.). Morgan Kaufmann. <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r886058088">[ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [1-55860-855-9](/wiki/Special:BookSources/1-55860-855-9 "Special:BookSources/1-55860-855-9").
*   Date, C. J. (1999), _[An Introduction to Database Systems](https://web.archive.org/web/20050404010227/http://www.aw-bc.com/catalog/academic/product/0,1144,0321197844,00.html)_ (8th ed.). Addison-Wesley Longman. <link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r886058088">[ISBN](/wiki/International_Standard_Book_Number "International Standard Book Number") [0-321-19784-4](/wiki/Special:BookSources/0-321-19784-4 "Special:BookSources/0-321-19784-4").
*   Kent, W. (1983) _[A Simple Guide to Five Normal Forms in Relational Database Theory](http://www.bkent.net/Doc/simple5.htm)_, Communications of the ACM, vol. 26, pp. 120–125

</div>

*   Codd, E.F. (1970). A Relational Model of Data for. Large Shared Data Banks. IBM Research Laboratory, San Jose, California.
*   Codd, E. F. (1971). Further Normalization of the Relational Model. Courant Computer Science Symposium 6 in Data Base Systems edited by Rustin, R.

<div role="navigation" class="navbox" aria-labelledby="Database_normalization" style="padding:3px">

<table class="nowraplinks collapsible autocollapse navbox-inner mw-collapsible mw-made-collapsible" style="border-spacing:0;background:transparent;color:inherit">

<tbody>

<tr>

<th scope="col" class="navbox-title" colspan="2"><span class="mw-collapsible-toggle mw-collapsible-toggle-default" role="button" tabindex="0"><a class="mw-collapsible-text">hide</a></span>

<div class="plainlinks hlist navbar mini">

*   [<abbr title="View this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">v</abbr>](/wiki/Template:Database_normalization "Template:Database normalization")
*   [<abbr title="Discuss this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">t</abbr>](/wiki/Template_talk:Database_normalization "Template talk:Database normalization")
*   [<abbr title="Edit this template" style=";;background:none transparent;border:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none; padding:0;">e</abbr>](//en.wikipedia.org/w/index.php?title=Template:Database_normalization&action=edit)

</div>

<div id="Database_normalization" style="font-size:114%;margin:0 4em">[Database normalization](/wiki/Database_normalization "Database normalization")</div>

</th>

</tr>

<tr>

<td colspan="2" class="navbox-list navbox-odd hlist" style="width:100%;padding:0px">

<div style="padding:0em 0.25em">

*   [Unnormalized form](/wiki/Unnormalized_form "Unnormalized form") (UNF/NF<sup>2</sup>)
*   <a class="mw-selflink selflink">First normal form</a> (1NF)
*   [Second normal form](/wiki/Second_normal_form "Second normal form") (2NF)
*   [Third normal form](/wiki/Third_normal_form "Third normal form") (3NF)
*   [Elementary key normal form](/wiki/Elementary_key_normal_form "Elementary key normal form") (EKNF)
*   [Boyce–Codd normal form](/wiki/Boyce%E2%80%93Codd_normal_form "Boyce–Codd normal form") (3.5NF / BCNF)
*   [Fourth normal form](/wiki/Fourth_normal_form "Fourth normal form") (4NF)
*   [Fifth normal form](/wiki/Fifth_normal_form "Fifth normal form") (5NF / PJNF)
*   [Domain-key normal form](/wiki/Domain-key_normal_form "Domain-key normal form") (DKNF)
*   [Sixth normal form](/wiki/Sixth_normal_form "Sixth normal form") (6NF)

</div>

</td>

</tr>

<tr>

<td class="navbox-abovebelow" colspan="2">

<div>[Denormalization](/wiki/Denormalization "Denormalization")</div>

</td>

</tr>

</tbody>

</table>

</div>

</div>

<noscript>![](//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1)</noscript>

</div>

<div class="printfooter">Retrieved from "[https://en.wikipedia.org/w/index.php?title=First_normal_form&oldid=895027109](https://en.wikipedia.org/w/index.php?title=First_normal_form&oldid=895027109)"</div>

<div id="catlinks" class="catlinks" data-mw="interface">

<div id="mw-normal-catlinks" class="mw-normal-catlinks">[Categories](/wiki/Help:Category "Help:Category"):

*   [Database normalization](/wiki/Category:Database_normalization "Category:Database normalization")

</div>

<div id="mw-hidden-catlinks" class="mw-hidden-catlinks mw-hidden-cats-hidden">Hidden categories:

*   [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
*   [Articles with unsourced statements from October 2018](/wiki/Category:Articles_with_unsourced_statements_from_October_2018 "Category:Articles with unsourced statements from October 2018")
*   [Wikipedia articles needing clarification from October 2018](/wiki/Category:Wikipedia_articles_needing_clarification_from_October_2018 "Category:Wikipedia articles needing clarification from October 2018")
*   [All articles with dead external links](/wiki/Category:All_articles_with_dead_external_links "Category:All articles with dead external links")
*   [Articles with dead external links from October 2017](/wiki/Category:Articles_with_dead_external_links_from_October_2017 "Category:Articles with dead external links from October 2017")
*   [Articles with permanently dead external links](/wiki/Category:Articles_with_permanently_dead_external_links "Category:Articles with permanently dead external links")

</div>

</div>

</div>
