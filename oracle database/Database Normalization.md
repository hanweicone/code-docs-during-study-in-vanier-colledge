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
*   [<span class="tocnumber">4</span> <span class="toctext">
</span>](#See_also)
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






</div>

</div>

</div>
