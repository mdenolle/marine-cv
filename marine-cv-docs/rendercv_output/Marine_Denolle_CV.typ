// Import the rendercv function and all the refactored components
#import "@preview/rendercv:0.1.0": *

// Apply the rendercv template with custom configuration
#show: rendercv.with(
  name: "Marine A. Denolle",
  footer: context { [#emph[Marine A. Denolle -- #str(here().page())\/#str(counter(page).final().first())]] },
  top-note: [ #emph[Last updated in 2026] ],
  locale-catalog-language: "en",
  page-size: "us-letter",
  page-top-margin: 0.7in,
  page-bottom-margin: 0.7in,
  page-left-margin: 0.3in,
  page-right-margin: 0.7in,
  page-show-footer: true,
  page-show-top-note: true,
  colors-body: rgb(0, 0, 0),
  colors-name: rgb(128, 0, 0),
  colors-headline: rgb(0, 79, 144),
  colors-connections: rgb(0, 0, 0),
  colors-section-titles: rgb(69, 128, 179),
  colors-links: rgb(0, 79, 144),
  colors-footer: rgb(128, 128, 128),
  colors-top-note: rgb(128, 128, 128),
  typography-line-spacing: 0.6em,
  typography-alignment: "justified",
  typography-date-and-location-column-alignment: right,
  typography-font-family-body: "IBM Plex Serif",
  typography-font-family-name: "Source Sans 3",
  typography-font-family-headline: "Source Sans 3",
  typography-font-family-connections: "Source Sans 3",
  typography-font-family-section-titles: "IBM Plex Sans",
  typography-font-size-body: 10pt,
  typography-font-size-name: 25pt,
  typography-font-size-headline: 10pt,
  typography-font-size-connections: 10pt,
  typography-font-size-section-titles: 1.4em,
  typography-small-caps-name: false,
  typography-small-caps-headline: false,
  typography-small-caps-connections: false,
  typography-small-caps-section-titles: false,
  typography-bold-name: false,
  typography-bold-headline: false,
  typography-bold-connections: false,
  typography-bold-section-titles: false,
  links-underline: true,
  links-show-external-link-icon: false,
  header-alignment: left,
  header-photo-width: 4.15cm,
  header-space-below-name: 0.7cm,
  header-space-below-headline: 0.7cm,
  header-space-below-connections: 0.7cm,
  header-connections-hyperlink: true,
  header-connections-show-icons: true,
  header-connections-display-urls-instead-of-usernames: false,
  header-connections-separator: "",
  header-connections-space-between-connections: 0.5cm,
  section-titles-type: "moderncv",
  section-titles-line-thickness: 0.15cm,
  section-titles-space-above: 0.55cm,
  section-titles-space-below: 0.3cm,
  sections-allow-page-break: true,
  sections-space-between-text-based-entries: 0.3em,
  sections-space-between-regular-entries: 1.2em,
  entries-date-and-location-width: 4.15cm,
  entries-side-space: 0cm,
  entries-space-between-columns: 0.3cm,
  entries-allow-page-break: false,
  entries-short-second-row: false,
  entries-summary-space-left: 0cm,
  entries-summary-space-above: 0.1cm,
  entries-highlights-bullet:  "•" ,
  entries-highlights-nested-bullet:  "•" ,
  entries-highlights-space-left: 0cm,
  entries-highlights-space-above: 0.15cm,
  entries-highlights-space-between-items: 0.1cm,
  entries-highlights-space-between-bullet-and-text: 0.3em,
  date: datetime(
    year: 2026,
    month: 1,
    day: 16,
  ),
)


= Marine A. Denolle

  #headline([Associate Professor, Earth and Space Sciences])

#connections(
  [#connection-with-icon("location-dot")[Seattle, WA]],
  [#link("mailto:mdenolle@uw.edu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[mdenolle\@uw.edu]]],
  [#link("https://denolle-lab.github.io/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[denolle-lab.github.io]]],
  [#link("https://github.com/mdenolle", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[mdenolle]]],
  [#link("https://github.com/Denolle-Lab", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[Denolle-Lab]]],
  [#link("https://orcid.org/0000-0002-1610-2250", icon: false, if-underline: false, if-color: false)[#connection-with-icon("orcid")[0000-0002-1610-2250]]],
  [#link("https://scholar.google.com/citations?user=GR8BOxsAAAAJ", icon: false, if-underline: false, if-color: false)[#connection-with-icon("graduation-cap")[Google Scholar]]],
)


== Research Impact Summary

#strong[Research Citations:] 3,398 total citations, h-index: 24, i10-index: 45 (Google Scholar)

#strong[Publications:] 66 peer-reviewed publications in Science, Nature Physics, AGU Advances, and top geophysics journals

#strong[Open-Source Software:] NoisePy (75 citations), SeisNoise.jl (26 citations), SeisIO.jl (11 citations)

#strong[Training Impact:] 500+ seismologists trained through workshops and courses

#strong[Data Products:] Global seismic phase database, PNW AI-ready dataset (35 citations)

== Education

#education-entry(
  [
    #strong[Stanford University], Geophysics

  ],
  [
    2008 – 2014

  ],
  main-column-second-row: [
    - Supervisor: Dr. Gregory Beroza

    - Co-supervisors: Dr. Eric Dunham, Dr. Jesse Lawrence

  ],
)

#education-entry(
  [
    #strong[Ecole Normale Supérieure - IPGP], Geophysics

  ],
  [
    2007 – 2008

  ],
  main-column-second-row: [
    - Supervisors: Dr. Satish Singh (IPGP), Dr. David Bercovici (Yale)

  ],
)

#education-entry(
  [
    #strong[Ecole Normale Supérieure], Earth Sciences

  ],
  [
    2006

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Lycée Chateaubriand, Rennes], Physics-Mathematics

  ],
  [
    2004 – 2005

  ],
  main-column-second-row: [
  ],
)

== Employment

#regular-entry(
  [
    #strong[Co-Founder]

  ],
  [
    Applied Environmental Intelligence

    Seattle

    2025 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Associate Professor]

    #summary[Department of Earth and Space Sciences]

  ],
  [
    University of Washington

    Seattle, WA

    2024 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Assistant Professor]

    #summary[Department of Earth and Space Sciences]

  ],
  [
    University of Washington

    Seattle, WA

    2021 – 2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Assistant Professor]

    #summary[Department of Earth and Planetary Sciences]

  ],
  [
    Harvard University

    Cambridge, MA

    2016 – 2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Green Postdoctoral Fellow]

    #summary[Institute of Geophysics and Planetary Physics]

    - Supervisor Dr. Peter Shearer

  ],
  [
    UC San Diego, Scripps Institution of Oceanography

    La Jolla, CA

    2014 – 2016

  ],
  main-column-second-row: [
  ],
)

== Awards

#education-entry(
  [
    #strong[Invited Professorship], Ecole Normale Supérieure rue d'Ulm-Paris

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Data Science Fellow], eScience Institute, University of Washington

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Charles F. Richter Early Career Award], Seismological Society of America

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Kavli Frontiers of Science Fellow], National Academy of Sciences

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Radcliffe Assistant Professorship], Institute for Advanced Study

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[CAREER Award], NSF

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[David and Lucile Packard Foundation Fellowship], David and Lucile Packard Foundation

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Outstanding Reviewer], Geophysical Research Letters

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Outstanding Reviewer], Geophysical Journal International

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[AGU Outstanding Student Paper Award], American Geophysical Union

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SSA Student Presentation Award], Seismological Society of America

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[AGU Outstanding Student Paper Award], American Geophysical Union

  ],
  [
    2010

  ],
  main-column-second-row: [
  ],
)

== Teaching

#regular-entry(
  [
    #strong[Machine Learning in the Geosciences]

    #link("https://geo-smart.github.io/mlgeo-book/")[geo-smart.github.io\/mlgeo-book]

    - Taught Fall 2021, 2022, 2023, 2024

  ],
  [
    ESS 469\/569

    U of Washington

    2021 - 2024

  ],
  main-column-second-row: [
    - Open-access Jupyter Book with asynchronous teaching materials

    - Course adopted by University of Arizona and UC Berkeley

    - Curated geoscience-specific ML datasets for homework

  ],
)

#regular-entry(
  [
    #strong[Computational\/Advanced Seismology]

    #link("https://denolle-lab.github.io/teaching/ess563/")[denolle-lab.github.io\/teaching\/ess563]

    - Taught Spring 2023, 2024, 2025

  ],
  [
    ESS 563

    U of Washington

    2023 - 2025

  ],
  main-column-second-row: [
    - Covers ambient noise seismology, earthquake source characterization

    - Julia and Python programming for high-performance computing

  ],
)

#regular-entry(
  [
    #strong[Introduction to Seismology]

    #link("https://denolle-lab.github.io/teaching/ess412/")[denolle-lab.github.io\/teaching\/ess412]

    - Taught Winter 2023, 2025, 2026

  ],
  [
    ESS 412\/512

    U of Washington

    2023 - 2026

  ],
  main-column-second-row: [
    - Covers earthquake physics, seismic waves, and hazard assessment

  ],
)

#regular-entry(
  [
    #strong[Geophysics]

    #link("https://github.com/UW-geophysics-edu/ESS314-fall23")[github.com\/UW-geophysics-edu\/ESS314-fall23]

    - Taught 2022, 2023, 2024, 2026

  ],
  [
    ESS 314

    U of Washington

    2022 - 2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Machine Learning in Earth and Planetary Sciences]

    - Taught Fall 2019

  ],
  [
    EPS 268

    Harvard

    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Induced Seismicity]

    - Taught Fall 2018

  ],
  [
    EPS 268

    Harvard

    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Earthquakes and Faulting]

    - Taught Fall 2018, 2020

  ],
  [
    EPS 203

    Harvard

    2018 - 2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Earthquakes and Tectonics]

    - Taught Fall 2017, 2020

  ],
  [
    EPS 55

    Harvard

    2017 - 2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Earthquake Sources]

    - Taught Spring 2016

  ],
  [
    EPS 204

    Harvard

    2016

  ],
  main-column-second-row: [
  ],
)

== Phd Advisees

#regular-entry(
  [
    #strong[Michael Hemmett]

    #summary[Offshore geophysics]

  ],
  [
    PhD Pre-Candidate

    UW ESS

    2025 - present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Manuela Koepfli]

    #summary[Geohazard assessment and early warning systems]

    - 1 publication, 1 in review, 1 in prep

  ],
  [
    PhD Candidate

    USS

    2022 - present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Akash Kharita]

    #summary[Geohazard characterization using machine learning]

    - 2 publications

  ],
  [
    PhD Pre-Candidate

    UW ESS

    2022 - present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Yiyu Ni]

    #summary[Machine learning and big data seismology]

    - 8 publications

  ],
  [
    PhD Candidate

    UW ESS

    2021 - present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Congcong Yuan]

    #summary[Time-dependent seismology, solid-fluid interaction. Next position: Cornell postdoc → Faculty position at NTU Singapore]

    - 4 publications

  ],
  [
    PhD

    Harvard

    2019 - 2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Stephanie Olinger]

    #summary[Cryo-seismology (50\% co-advised with Brad Lipovsky). Next position: Stanford Thompson Postdoctoral Fellowship → CEO of AEI]

    - 4 publications

  ],
  [
    PhD

    Harvard

    2018 - 2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Tim Clements]

    #summary[Hydro-seismology and big-data seismology. Next position: USGS Mendenhall Postdoc → USGS Research Geophysicist]

    - 4 publications

  ],
  [
    PhD

    Harvard

    2016 - 2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Jiuxun Yin]

    #summary[Earthquake seismology and source characterization. Next position: Caltech SCSN Postdoc Fellowship → Schlumberger]

    - 6 publications

  ],
  [
    PhD

    Harvard

    2016 - 2022

  ],
  main-column-second-row: [
  ],
)

== Other Graduate Student Supervision

#strong[Note:] (#sym.ast.basic#h(0pt, weak: true) ) At UW, roles are secondary advisor or primary advisor on one project\/manuscript. (#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ) Advising resulted in a peer-reviewed publication.

#strong[Maleen Kidiwela (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):]  2021-present, UW Oceanography (co-advised with William Wilcock) - DAS and offshore seismology, resulted in publication

#strong[Zoe Krauss (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2021-2024, UW Oceanography (co-advised with William Wilcock) - Axial Seamount hydrothermal monitoring, resulted in publication

#strong[Parker Sprinkle (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2021-present, UW ESS (co-advised) - Earthquake early warning and machine learning

#strong[Natasha Toghramadjian (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2018-2025, Harvard EPS - Seismic attenuation and site effects, resulted in publications

#strong[Zhuo Yang (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2018-2021, Harvard EPS - Machine learning for seismic phase picking, resulted in publication

#strong[William Flanagan (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2019, Harvard EPS - Volcano seismology project

#strong[Thibault Pérol (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2017, Harvard EPS - Deep learning for earthquake detection, resulted in multiple publications

#strong[Congcong Yuan (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ) :] 2019, USTC China - Master student visiting researcher on time-dependent seismology, resulted in publication

#strong[Philippe Danré (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2018, Ecole Normale Supérieure Paris - Master thesis on seismic monitoring, resulted in publication

#strong[Manuel Florez (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ):] 2017-2019, MIT - Dissertation committee member for geophysics PhD

== Graduate Student Committees

#strong[Koepfli, Manuela:] Earth and Space Sciences, Chair, 2024-present

#strong[Ni, Yiyu:] Earth and Space Sciences, Chair, 2024-present

#strong[Kharita, Akash:] Earth and Space Sciences, Advisor, 2023-present

#strong[DeGrande, Jensen:] Earth and Space Sciences, Member, 2023-present

#strong[Pearson, Anna Elaine Rogers:] Earth and Space Sciences, Member, 2024-present

#strong[Sprinkle, Parker:] Earth and Space Sciences, Member, 2022-present

#strong[Kidiwela, Maleen:] School of Oceanography, Member, 2024-present

#strong[Krauss, Zoe:] School of Oceanography, GSR, 2022-2024

#strong[Sangmin, Song:] School of Oceanography, GSR, 2024-present

#strong[Zhang, Maochuan:] School of Oceanography, GSR, 2023-present

#strong[Jones, Randall:] Atmospheric Sciences, GSR, 2025-present

#strong[Chien, Mu-Ting:] Atmospheric Sciences, GSR, 2023-2024

#strong[Sweeney, Aodhan:] Atmospheric Sciences, GSR, 2024-present

#strong[Ragland, John:] Electrical and Computer Engineering, GSR, 2023-2024

#strong[Rasanen, Ryan:] Civil and Environmental Engineering, GSR, 2022-2023

#strong[Velappan, Hemalatha:] School of Environmental and Forest Sciences, GSR, 2023-present

#strong[Velegar, Meghana S:] Applied Mathematics, GSR, 2023-2023

#strong[Zahn, Olivia:] Physics, GSR, 2022-2024

== International Phd Advising

#strong[Note:] Dissertation and defense evaluating committee members

#strong[Marius Paul Isken :] 2024 (GFZ, Germany)

#strong[Luc Illien :] 2023 (GFZ, Germany)

#strong[Zoe Renate :] 2023 (Universite de Lorraine, France)

#strong[Reza Esfahani :] 2022 (GFZ, Germany)

#strong[Kurama Okubo :] 2019 (ENS, Paris, France)

== Media Coverage


- #link("https://youtu.be/Q6Gt0-S_9WA?si=pz6REZqXWsolYXjc")[2025 Global-scale Database of Seismic Phases]



- #link("https://youtu.be/oG4_MrOfums?si=bw6AwACloHAjqTU1")[2024 Ambient Field Monitoring in the Shallow Crust]



- #link("https://youtu.be/nZ2qozO0VVs?si=pPCX3nAduKDX8GGJ")[2024 Making Big Data Look Small]



- #link("https://youtu.be/iRJliquttKg?si=NgscKZLTdOZ0cE9K")[2023 UW eScience Seminar]



- #link("https://youtu.be/WeZ2vJxBuTg?si=hNuIRAPEjxtYAsJG")[2023 Open Science in Seismology]



- #link("https://youtu.be/ff-AJRic0HY?si=Lnzyw0Ih7K87lLw7")[2023 UW News Fiber Sensing]



- #link("https://youtu.be/-1GbSmiOt70?si=OExw9eGY7pMXEP67")[2018 Radcliffe Seminar: Where we stand in Earthquake Prediction]


== Undergraduate Students

#strong[Note:] My undergraduate advising includes research opportunities through summer programs and independent studies (ESS 499 for credit during academic year, hourly pay during summer\/breaks). I mentor students toward conference presentations and publications, and support competitive fellowship applications. Legend: (#sym.ast.basic#h(0pt, weak: true) ) Conference presentation | (#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ) Peer-reviewed publication | (#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ) Publication in prep | (+) NSF GRFP recipient

#strong[Alex Rose :] 2025-present, UW Oceanography - DAS data processing research

#strong[Anjani Mirchandi:] 2024-present, UW Applied Math - DAS data processing research

#strong[Hiroto Bito:] 2023-2026, UW ESS - ML for earthquake catalog building and spatio-temporal forecasting

#strong[Nicholas Wolfe:] 2023, UW ESS - Earthquake magnitude estimation project

#strong[Informatics Capstone Team (lead Rona Guo(#sym.ast.basic#h(0pt, weak: true) )):] 2023, Nathan Limono, William Phan, Michael Yung, Matthew Herradura), UW Informatics - DAS Platform development, resulted in conference presentation

#strong[Lucas Swanson :] 2023, UW Informatics - DAS software development

#strong[Francesca Skene (#sym.ast.basic#h(0pt, weak: true) ) :] 2022-2023, UW ESS - Surface event catalog, resulted in conference presentation

#strong[Nick Smoczyk (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ) :] 2022-2024, University of Minnesota - Volcano seismology using RedPy catalog, resulted in conference presentation and publication in prep

#strong[Julian Schmitt (#sym.ast.basic#h(0pt, weak: true) ,+) :] 2020-2021, Harvard EPS - Ambient noise seismology on cloud computing with Julia, BASIN project, resulted in conference presentation and NSF GRFP

#strong[Jared Bryan (#sym.ast.basic#h(0pt, weak: true) ,#sym.ast.basic#h(0pt, weak: true) #sym.ast.basic#h(0pt, weak: true) ,+):] 2019, Harvard EPS - Ambient noise monitoring, SCEC Internship, resulted in conference presentation, publication, and NSF GRFP

#strong[Albert Aguilar (#sym.ast.basic#h(0pt, weak: true) ):] 2018, Harvard EPS - Subduction zone seismology and data mining, SCEC, resulted in conference presentation

#strong[Leore Lavin:] 2016, Harvard EPS - Ground motion simulations with ambient noise

#strong[Roy Bowling (#sym.ast.basic#h(0pt, weak: true) ):] 2014, Scripps IGPP - Ambient noise seismology, SCEC Internship

#strong[Tara Larrue (#sym.ast.basic#h(0pt, weak: true) ):] 2012, Stanford Geophysics - Ambient noise seismology, SURGE program

#strong[Penprapa Wutthijuk (#sym.ast.basic#h(0pt, weak: true) ):] 2011, Stanford - Ambient noise seismology, SURGE program

== Training Workshops

#regular-entry(
  [
    #summary[co-PI organizer for ML and Earthquake Catalog Building workshop (35 participants)]

  ],
  [
    2025

  ],
  main-column-second-row: [
    #link("https://scoped-mlscience-book.readthedocs.io/")[scoped-mlscience-book.readthedocs.io]

  ],
)

#regular-entry(
  [
    #summary[Lead PI organizer for Cloud\/HPC\/wavefield simulations workshop (100 participants)]

  ],
  [
    2024

  ],
  main-column-second-row: [
    #link("https://seisscoped.org/HPS-book/intro.html")[seisscoped.org\/HPS-book\/intro.html]

  ],
)

#regular-entry(
  [
    #summary[Lead organizer of cloud workshop (80 participants)]

  ],
  [
    2024

  ],
  main-column-second-row: [
    #link("https://seisscoped.org/SSA-Cloud-101/intro.html")[seisscoped.org\/SSA-Cloud-101\/intro.html]

  ],
)

#regular-entry(
  [
    #summary[Lead PI, coordinator, and instructor for HPC and Data Science]

  ],
  [
    2023

  ],
  main-column-second-row: [
    #link("https://seisscoped.org/HPS-book/intro.html")[seisscoped.org\/HPS-book\/intro.html]

  ],
)

#regular-entry(
  [
    #summary[Co-organizer of ML training with Jupyter Book]

  ],
  [
    2021 – present

  ],
  main-column-second-row: [
    #link("https://geo-smart.github.io/mlgeo-book/")[geo-smart.github.io\/mlgeo-book]

  ],
)

#regular-entry(
  [
    #summary[Scientific committee member and instructor]

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

== University Service

#regular-entry(
  [
    #strong[Department Colloquium Committee]

    - Help organizing the department colloquium series

  ],
  [
    University of Washington

    2026 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[AI\@UW Advisory Committee to the VP]

    - Advising AI strategy and initiatives across the university

  ],
  [
    University of Washington

    2026 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Co-director of UW CS4Env]

    - Computer Science for the Environment (CS4Env) is a cross-unit initiative to promote synergies between computer science and environmental research at UW, includes organizing biweekly seminar, reviewing proposals, and organizing an annual symposium.

  ],
  [
    University of Washington

    2024 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Chair of Curriculum Committee]

    - Reviewing proposed courses, course changes, undergraduate and graduate program.

  ],
  [
    UW\/ESS

    2024 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member of Curriculum Committee and Data Science Oversight Committee]

    - Review the proposed data science option program

  ],
  [
    UW\/ESS

    2022 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member of Executive Committee]

  ],
  [
    UW\/ESS

    2022 – 2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member of Research Faculty Search Committees]

    - Search committee for PNSN Network Manager and Igneous Processes Faculty Search

  ],
  [
    UW\/ESS

    2022 – 2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Multiple Committee Memberships]

    - Undergraduate Curriculum Committee, Graduate Student Council, IT Committee, Diversity Inclusion and Belonging Committee, Department Colloquium Committee

  ],
  [
    Harvard University

    2016 – 2020

  ],
  main-column-second-row: [
  ],
)

== Professional Service

#regular-entry(
  [
    #strong[Member]

  ],
  [
    Earthscope Consortium - Board of Directors

    2026 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Chair]

  ],
  [
    Earthscope Consortium Integration and Innovation Advisory Committee

    2023 – 2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member]

  ],
  [
    SCEC Science Steering Committee

    2024 – 2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member]

  ],
  [
    IRIS Data Service Standing Committee

    2021 – 2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member]

  ],
  [
    SCEC HPC Standing Committee

    2021 – 2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Chair]

  ],
  [
    Graduate Student Council, Stanford University

    2011 – 2012

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Committee Member]

  ],
  [
    Charles Richter Early Career Award Committee

    2022 – present

  ],
  main-column-second-row: [
  ],
)

== Review Panels

#regular-entry(
  [
    #strong[NSF Review Panels]

    - Reviewed 10+ proposals per panel

  ],
  [
    Geophysics Program

    2020 – 2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[USGS Review Panels]

    - Reviewed 10+ proposals per panel

  ],
  [
    Earthquake Hazards Program

    2016 – 2018

  ],
  main-column-second-row: [
  ],
)

== Editorial Service

#regular-entry(
  [
    #strong[Editor]

  ],
  [
    Geophysical Journal International

    2025 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Associate Editor]

  ],
  [
    Geophysical Research Letters

    2017 – 2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Reviewer]

    - \>150 reviews for GJI, BSSA, Nature Communications, GRL, JGR, Science, and others

  ],
  [
    Multiple Journals

    2014 – present

  ],
  main-column-second-row: [
  ],
)
