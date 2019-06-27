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

