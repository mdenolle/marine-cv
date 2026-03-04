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
  typography-font-family-body: "Libertinus Serif",
  typography-font-family-name: "Source Sans 3",
  typography-font-family-headline: "Source Sans 3",
  typography-font-family-connections: "Source Sans 3",
  typography-font-family-section-titles: "Open Sans",
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
  sections-space-between-regular-entries: 0.6em,
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

  #headline([Associate Professor, Earth and Space Sciences, University of Washington])

#connections(
  [#connection-with-icon("location-dot")[Seattle, WA]],
  [#link("mailto:mdenolle@uw.edu", icon: false, if-underline: false, if-color: false)[#connection-with-icon("envelope")[mdenolle\@uw.edu]]],
  [#link("https://www.denolle.ai/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("link")[www.denolle.ai]]],
  [#link("https://github.com/mdenolle", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[mdenolle]]],
  [#link("https://github.com/Denolle-Lab", icon: false, if-underline: false, if-color: false)[#connection-with-icon("github")[Denolle-Lab]]],
  [#link("https://orcid.org/0000-0002-1610-2250", icon: false, if-underline: false, if-color: false)[#connection-with-icon("orcid")[0000-0002-1610-2250]]],
  [#link("https://scholar.google.com/citations?user=GR8BOxsAAAAJ", icon: false, if-underline: false, if-color: false)[#connection-with-icon("graduation-cap")[Google Scholar]]],
  [#link("https://youtube.com/@scoped6259", icon: false, if-underline: false, if-color: false)[#connection-with-icon("youtube")[scoped6259]]],
  [#link("https://youtube.com/@uwgeophysics6888", icon: false, if-underline: false, if-color: false)[#connection-with-icon("youtube")[uwgeophysics6888]]],
  [#link("https://denolle-lab.github.io/", icon: false, if-underline: false, if-color: false)[#connection-with-icon("flask")[denolle-lab.github.io]]],
)


== Research Impact Summary

#strong[Research Citations:] 3,398 total (h-index: 24, i10: 45) | 2,291 last-5y (h₅: 22, i10₅: 43) | Google Scholar

#strong[Publications:] 66 peer-reviewed | 7 Nature\/Science-family (T1) | 40 AGU-flagship (T2) | 15 domain journals (T3) | 1 reviews\/perspectives | 3 preprints

#strong[Research Funding:] Lead PI: \$3.1M (14 grants) | Co-PI\/Co-I: \$4.9M (8 grants) | Fellowships: \$878K (2)

#strong[Open-Source Software:] 372 GitHub stars | 241 forks | 18 active repos | NoisePy: 207 stars, 83 forks, 19 contributors | 1,692+ PyPI downloads\/yr

#strong[Mentoring:] 8 PhD (4 current, 4 graduated) | 11 postdocs | 15+ undergrads | 10 co-supervised grad students | 5 became faculty

#strong[Broader Impact:] 6 workshops, 215+ seismologists trained | mlgeo-book: 11 GitHub stars

== Education

#education-entry(
  [
    #strong[Stanford University] Geophysics

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
    #strong[Ecole Normale Supérieure - IPGP] Geophysics

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
    #strong[Ecole Normale Supérieure] Earth Sciences

  ],
  [
    2006

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Lycée Chateaubriand, Rennes] Physics-Mathematics

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
    #strong[Invited Professorship] Ecole Normale Supérieure rue d'Ulm-Paris

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Data Science Fellow] eScience Institute, University of Washington

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Charles F. Richter Early Career Award] Seismological Society of America

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Kavli Frontiers of Science Fellow] National Academy of Sciences

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Radcliffe Assistant Professorship] Institute for Advanced Study

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[CAREER Award] NSF

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[David and Lucile Packard Foundation Fellowship] David and Lucile Packard Foundation

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Outstanding Reviewer] Geophysical Research Letters

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Outstanding Reviewer] Geophysical Journal International

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[AGU Outstanding Student Paper Award] American Geophysical Union

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SSA Student Presentation Award] Seismological Society of America

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[AGU Outstanding Student Paper Award] American Geophysical Union

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

== Postdocs

#regular-entry(
  [
    #strong[Dr. Qibin Shi]

    #summary[DAS, Deep Learning, Earthquake Catalog building, AgroSeismology]

  ],
  [
    University of Washington

    2022 - 2024

  ],
  main-column-second-row: [
    - Now Postdoctoral Fellow at Rice University

  ],
)

#regular-entry(
  [
    #strong[Dr. Kuan-Fu Feng]

    #summary[Environmental Seismology, Cloud computing]

  ],
  [
    University of Washington

    2023 - 2024

  ],
  main-column-second-row: [
    - Next position: Postdoc at University of Utah

  ],
)

#regular-entry(
  [
    #strong[Dr. Ethan Williams]

    #summary[DAS]

  ],
  [
    University of Washington

    2023 - 2025

  ],
  main-column-second-row: [
    - Next position: Assistant Professor at UC Santa Cruz

  ],
)

#regular-entry(
  [
    #strong[Dr. Stephanie Olinger]

    #summary[Cryoseismology, DAS, Ambient noise monitoring]

  ],
  [
    University of Washington

    2024 - 2025

  ],
  main-column-second-row: [
    - Next position: Climate Tech → CEO Applied Environmental Intelligence

  ],
)

#regular-entry(
  [
    #strong[Dr. Laura Ermert]

    #summary[Environmental seismology]

  ],
  [
    Harvard University\/University of Washington

    2020 - 2022

  ],
  main-column-second-row: [
    - Next position: Assistant Professor at ISTerre

  ],
)

#regular-entry(
  [
    #strong[Dr. Xiaotao Yang]

    #summary[Ambient noise cross correlation]

  ],
  [
    Harvard University

    2019 - 2020

  ],
  main-column-second-row: [
    - Next position: Assistant Professor at Purdue

  ],
)

#regular-entry(
  [
    #strong[Dr. Kurama Okubo]

    #summary[Ambient noise monitoring]

  ],
  [
    Harvard University

    2019 - 2020

  ],
  main-column-second-row: [
    - Next position: Researcher at NIED, Japan

  ],
)

#regular-entry(
  [
    #strong[Dr. Zhitu Ma]

    #summary[Ambient noise cross correlation]

  ],
  [
    Harvard University

    2019 - 2020

  ],
  main-column-second-row: [
    - Next position: Assistant Professor at Tongji University, China

  ],
)

#regular-entry(
  [
    #strong[Dr. Chengxin Jiang]

    #summary[Ambient noise seismology, computational seismology]

  ],
  [
    Harvard University

    2018 - 2019

  ],
  main-column-second-row: [
    - Next position: Research Associate at Australian National University

  ],
)

#regular-entry(
  [
    #strong[Dr. Chris Van Houtte]

    #summary[Earthquake Source seismology]

  ],
  [
    Harvard University

    2016 - 2017

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Dr. Loïc Viens]

    #summary[ambient noise seismology, ground motion prediction]

  ],
  [
    Harvard University

    2016 - 2018

  ],
  main-column-second-row: [
    - Next position Researcher at Los Alamos

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
    (2025).

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    (2024).

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    (2024).

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    (2023).

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    (2021 – present).

  ],
  [
    2021 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    (2016).

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
    #strong[Member of Board of Directors at Earthscope Consortium]

  ],
  [
    2026 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Chair of Integration and Innovation Advisory Committee at Earthscope Consortium]

  ],
  [
    2023 – 2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member of Science Steering Committee at SCEC]

  ],
  [
    2024 – 2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member of Data Service Standing Committee at IRIS]

  ],
  [
    2021 – 2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Member of HPC Standing Committee at SCEC]

  ],
  [
    2021 – 2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Chair of Graduate Student Council at Stanford University]

  ],
  [
    2011 – 2012

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Committee Member of Charles Richter Early Career Award Committee at Seismological Society of America]

  ],
  [
    2022 – 2022

  ],
  main-column-second-row: [
  ],
)

== Review Panels

#regular-entry(
  [
    #strong[NSF Review Panels EAR-Geophysics and GeoInformatics]

  ],
  [
    2020,2024

  ],
  main-column-second-row: [
    - Reviewed 10+ proposals per panel

  ],
)

#regular-entry(
  [
    #strong[USGS Review Panels Earthquake Hazards Program]

  ],
  [
    2016 – 2018

  ],
  main-column-second-row: [
    - Reviewed 10+ proposals per panel

  ],
)

== Editorial Service

#regular-entry(
  [
    #strong[Editor at Geophysical Journal International]

  ],
  [
    2025 – present

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Associate Editor at Geophysical Research Letters]

  ],
  [
    2017 – 2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Reviewer for multiple journals in geophysics and seismology]

  ],
  [
    2014 – present

  ],
  main-column-second-row: [
    - \>150 reviews for GJI, BSSA, Nature Communications, GRL, JGR, Science, and others

  ],
)

== Publications Legend

#strong[Author Notation:] #strong[Bold]: Marine A. Denolle (PI). #emph[Italic]: graduate students, postdocs, and undergraduate students mentored by MD.

== Publications

#regular-entry(
  [
    Veronica Gaete-Elgueta, #emph[Manuela Köpfli], Dominik Gräff, Bradley P Lipovsky, #strong[Marine A. Denolle], Weston A. Thelen, Brendan Pratt, Taylor R. Kenyon (2026). #strong[Distributed Acoustic Sensing Records of Earthquakes and Surface Processes at Mount Rainier Volcano]. in review in Seismica

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    John Townend, Ilma Del Carmen Juarez-Garfias, Olivia Pita-Sllim, Calum J. Chamberlain, Emily Warren-Smith, Caroline Holden, Kasper van Wijk, #strong[Marine Denolle], Andrew Curtis, Hiroe Miyake (2026). #strong[Seismological Analysis of Contemporary and Future Alpine Fault Earthquakes Using the Southern Alps Long Skinny Array (SALSA)]. in press in Seismological Research Letters

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Natasha Toghramadjian], #strong[Marine A. Denolle], #emph[Laura Ermert], #emph[Chengxin Jiang] (2026). #strong[Probing the Seattle Basin Edge Using a Dense Urban Nodal Array in 100 Backyards]. Seismological Research Letters, #link("https://doi.org/10.1785/0220250241")[10.1785\/0220250241]

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    Alexey Yermakov, Yue Zhao, #strong[Marine Denolle], #emph[Yiyu Ni], Philippe M. Wyder, Judah Goldfeder, Stefano Riva, #emph[Jan Williams], David Zoro, Amy Sara Rude, Matteo Tomasetto, Joe Germany, Joseph Bakarji, Georg Maierhofer, Miles Cranmer, J. Nathan Kutz (2026). #strong[The Seismic Wavefield Common Task Framework]. arXiv, #link("https://doi.org/10.48550/arXiv.2512.19927")[10.48550\/arXiv.2512.19927]

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Qibin Shi], David Montgomery, Abigail L.S. Swann, Nicoleta C. Cristea, #emph[Ethan Williams], Nan You, Joe Collins, Ana Prada Barrio, Simon Jeffrey, Ana Misiewicz, Tarje Nissen-Meyer, #strong[Marine A. Denolle] (2026). #strong[Agroseismology: unraveling the impact of farming practices on soil hydrodynamics]. in review in Science - preprint on Arxiv, #link("https://doi.org/10.48550/arXiv.2509.09821")[10.48550\/arXiv.2509.09821]

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Kuan-Fu Feng], #strong[Marine Denolle], Fan-Chi Lin, Tonie van Dam (2026). #strong[A Decadal Survey of the Near-Surface Seismic Velocity Response to Hydrological Variations in Utah, United States]. Journal of Geophysical Research: Solid Earth, 131

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Akash Kharita], #strong[Marine Denolle], Alexander R Hutko, J Renate Hartog, Stephen D Malone (2025). #strong[Exploration of Machine Learning Methods to Seismic Event Discrimination in the Pacific Northwest]. accepted in Seismica, pre-print on Arxiv, #link("https://doi.org/10.48550/arXiv.2510.23795")[10.48550\/arXiv.2510.23795]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Yiyu Ni], #strong[Marine Denolle], Amanda Thomas, Alex Hamilton, Jannes Münchmeyer, Yinzhi Wang, Loïc Bachelot, Chad Trabant, David Mencin (2025). #strong[A Global-scale Database of Seismic Phases from Cloud-based Picking at Petabyte Scale]. Seismica, 4, #link("https://doi.org/10.26443/seismica.v4i2.1738")[10.26443\/seismica.v4i2.1738]

  ],
  [
    2025

  ],
  main-column-second-row: [
    Featured in: #link("https://youtu.be/Q6Gt0-S_9WA?si=pz6REZqXWsolYXjc")[Video]

  ],
)

#regular-entry(
  [
    #emph[Yiyu Ni], #strong[Marine A Denolle], Jannes Münchmeyer, Yinzhi Wang, #emph[Kuan-Fu Feng], Carlos Garcia Jurado Suarez, Amanda M Thomas, Chad Trabant, Alex Hamilton, David Mencin (2025). #strong[A Review of Cloud Computing and Storage in Seismology]. Geophysical Journal International, #link("https://doi.org/10.1093/gji/ggaf322")[10.1093\/gji\/ggaf322]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Marine A. Denolle], Carl Tape, Ebru Bozdağ, Yinzhi Wang, Felix Waldhauser, Alice‐Agnes Gabriel, Jochen Braunmiller, Bryant Chow, Liang Ding, #emph[Kuan‐Fu Feng], Ayon Ghosh, Nathan Groebner, Aakash Gupta, #emph[Zoe Krauss], Amanda M. McPherson, Masaru Nagaso, Zihua Niu, #emph[Yiyu Ni], Rıdvan Örsvuran, Gary Pavlis, Felix Rodriguez‐Cardozo, Theresa Sawi, David Schaff, Nico Schliwa, David Schneller, #emph[Qibin Shi], Julien Thurin, Chenxiao Wang, Kaiwen Wang, Jeremy Wing Ching Wong, Sebastian Wolf, #emph[Congcong Yuan] (2025). #strong[Training the Next Generation of Seismologists: Delivering Research‐Grade Software Education for Cloud and HPC Computing Through Diverse Training Modalities]. Seismological Research Letters, 96, #link("https://doi.org/10.1785/0220240413")[10.1785\/0220240413]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Marine A. Denolle], #emph[Qibin Shi], #emph[Tim Clements], #emph[Loïc Viens], Veronica Rodriguez-Tribaldos, Fabrice Cotton (2025). #strong[Ambient field seismology in critical zone hydrological sciences]. Comptes Rendus. Géoscience, 357, #link("https://doi.org/10.5802/crgeos.310")[10.5802\/crgeos.310]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Q. Shi], #strong[M. A. Denolle], #emph[Y. Ni], #emph[E. F. Williams], N. You (2025). #strong[Denoising Offshore Distributed Acoustic Sensing Using Masked Auto-Encoders to Enhance Earthquake Detection]. JGR: Solid Earth, 130, #link("https://doi.org/10.1029/2024JB029728")[10.1029\/2024JB029728]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Q. Shi], #emph[E. F. Williams], B. P. Lipovsky, #strong[M. A. Denolle], W. S. D. Wilcock, D. S. Kelley, K. Schoedl (2025). #strong[Multiplexed Distributed Acoustic Sensing Offshore Central Oregon]. Seismological Research Letters, 96, #link("https://doi.org/10.1785/0220240460")[10.1785\/0220240460]

  ],
  [
    2025

  ],
  main-column-second-row: [
    Featured in: #link("https://www.washington.edu/news/2025/07/24/seismologists-use-fiber-optic-cables-to-study-offshore-faults/")[UW News], #link("https://phys.org/news/2025-07-ai-fiber-optics-reveal-hidden.html")[Phys]

  ],
)

#regular-entry(
  [
    #emph[Y. Ni], #strong[M. A. Denolle], #emph[Q. Shi], B. P. Lipovsky, S. Pan, J. N. Kutz (2024). #strong[Wavefield reconstruction of distributed acoustic sensing: Lossy compression, wavefield separation, and edge computing]. Journal of Geophysical Research: Machine Learning and Computation, 1, #link("https://doi.org/10.1029/2024JH000247")[10.1029\/2024JH000247]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    P. Makus, #strong[M. A. Denolle], C. Sens-Schönfelder, #emph[M. Köpfli], F. Tilmann (2024). #strong[Analysing Volcanic, Tectonic, and Environmental Influences on the Seismic Velocity from 25 Years of Data at Mount St. Helens]. Seismological Research Letters, 95, #link("https://doi.org/10.1785/0220240088")[10.1785\/0220240088]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    M. Köpli, #strong[M. A. Denolle], W. Thelen, P. Makus, S. Malone (2024). #strong[Examining 22 Years of Ambient Seismic Wavefield at Mount St. Helens]. Seismological Research Letters, 95, #link("https://doi.org/10.1785/0220240079")[10.1785\/0220240079]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    F. Diewald, #strong[M. Denolle], J. J. Timothy, C. Gehlen (2024). #strong[Impact of Temperature and Relative Humidity Variations on Coda Waves in Concrete]. Scientific Reports, 14, #link("https://doi.org/10.1038/s41598-024-69564-4")[10.1038\/s41598-024-69564-4]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[K. Okubo], B. Delbridge, #strong[M. Denolle] (2024). #strong[Monitoring velocity change over 20 years at Parkfield]. Journal of Geophysical Research: Solid Earth, 129, #link("https://doi.org/10.1029/2023JB028084")[10.1029\/2023JB028084]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    T. Cochard, I. Svetlizky, G. Albertini, R. C. Viesca, S. M. Rubinstein, F. Spaepen, #emph[C. Yuan], #strong[M. Denolle], Y.-Q. Song, L. Xiao, D. A. Weitz (2024). #strong[Extended crack propagation by local nucleation and rapid transverse expansion]. Nature Physics, #link("https://doi.org/10.1038/s41567-023-02365-0")[10.1038\/s41567-023-02365-0]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[A. Kharita], #strong[M. Denolle], M. West (2023). #strong[Discrimination between icequakes and earthquakes in southern Alaska: an exploration of waveform features using random forest algorithm]. Geophysical Journal International, #link("https://doi.org/10.1093/gji/ggae106")[10.1093\/gji\/ggae106]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[S. Olinger], B. Lipovsky, #strong[M. Denolle] (2023). #strong[Ocean Coupling Limits Rupture Velocity of Fastest Observed Ice Shelf Rift Propagation Event]. AGU Advances, 5, #link("https://doi.org/10.1029/2023AV001023")[10.1029\/2023AV001023]

  ],
  [
    2023

  ],
  main-column-second-row: [
    Featured in: #link("https://www.washington.edu/news/2024/02/28/80-mph-speed-record-for-glacier-fracture-helps-reveal-the-physics-of-ice-sheet-collapse/")[UW News], #link("https://eos.org/editor-highlights/speed-of-ice-shelf-rifting-controlled-by-ocean-ice-interactions")[EOS]

  ],
)

#regular-entry(
  [
    #emph[C. Yuan], T. Cochard, #strong[M. Denolle], J. Gomberg, A. Wech, L. Xiao, D. Weitz (2023). #strong[Laboratory hydrofracture as analogs to tectonic tremors]. AGU Advances, 5, #link("https://doi.org/10.1029/2023AV001002")[10.1029\/2023AV001002]

  ],
  [
    2023

  ],
  main-column-second-row: [
    Featured in: #link("https://www.washington.edu/news/2024/01/29/qa-how-slow-slip-earthquakes-may-be-driven-by-deep-hydraulic-fracturing/")[UW News], #link("https://eos.org/research-spotlights/scientists-model-whats-moving-beneath-earths-surface")[EOS]

  ],
)

#regular-entry(
  [
    #emph[Q. Shi], #strong[M. Denolle] (2023). #strong[Improved observations of deep earthquake ruptures using machine learning]. Journal of Geophysical Research: Solid Earth, 128, #link("https://doi.org/10.1029/2023JB027334")[10.1029\/2023JB027334]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Congcong Yuan], #emph[Yiyu Ni], Youzuo Lin, #strong[Marine Denolle] (2023). #strong[Better Together: Ensemble Learning for Earthquake Detection and Phase Picking]. IEEE Transactions on Geoscience and Remote Sensing, 61, #link("https://doi.org/10.1109/TGRS.2023.3320148")[10.1109\/TGRS.2023.3320148]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Yiyu Ni], #strong[Marine A. Denolle], Rob Fatland, Naomi Alterman, Bradley P. Lipovsky, Friedrich Knuth (2023). #strong[An Object Storage for Distributed Acoustic Sensing]. Seismological Research Letters, 95, #link("https://doi.org/10.1785/0220230172")[10.1785\/0220230172]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Z. Krauss], #emph[Y. Ni], S. Henderson, #strong[M. Denolle] (2023). #strong[Seismology in the cloud: guidance for the individual researcher]. Seismica, 2, #link("https://doi.org/10.26443/seismica.v2i2.979")[10.26443\/seismica.v2i2.979]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Y. Ni], A. Hutko, #emph[F. Skene], #strong[M. Denolle], S. Malone, P. Bodin, R. Hartog, A. Wright (2023). #strong[Curated Pacific Northwest AI-ready Seismic Dataset]. Seismica, 2, #link("https://doi.org/10.26443/seismica.v2i1.368")[10.26443\/seismica.v2i1.368]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Ermert], E. Cabral-Cano, E. Chaussard, D. Solano-Rojas, L. Quintanar, D. Morales Padilla, E. A. Fernandez-Torres, #strong[M. A. Denolle] (2023). #strong[Probing environmental and tectonic changes underneath Ciudad de México with the urban seismic field]. Solid Earth (EGU), #link("https://doi.org/10.5194/egusphere-2022-1361")[10.5194\/egusphere-2022-1361]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Clements], #strong[M. A. Denolle] (2023). #strong[The Seismic Signature of California's Earthquakes, Droughts, and Floods]. Journal of Geophysical Research: Solid Earth, 128, #link("https://doi.org/10.1029/2022JB025553")[10.1029\/2022JB025553]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], #strong[M. A. Denolle], B. He (2022). #strong[A multitask encoder--decoder to separate earthquake and ambient noise signal in seismograms]. Geophysical Journal International, 231, #link("https://doi.org/10.1093/gji/ggac290")[10.1093\/gji\/ggac290]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[C. Jiang], #strong[M. A. Denolle] (2022). #strong[Pronounced Seismic Anisotropy in Kanto Sedimentary Basin: A Case Study of Using Dense Arrays, Ambient Noise Seismology, and Multi-Modal Surface-Wave Imaging]. Journal of Geophysical Research: Solid Earth, 127, #link("https://doi.org/10.1029/2022JB024613")[10.1029\/2022JB024613]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Viens], #emph[C. Jiang], #strong[M. A. Denolle] (2022). #strong[Imaging the Kanto Basin seismic basement with earthquake and noise autocorrelation functions]. Geophysical Journal International, 230, #link("https://doi.org/10.1093/gji/ggac101")[10.1093\/gji\/ggac101]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[S. D. Olinger], B. P. Lipovsky, #strong[M. A. Denolle], B. W. Crowell (2022). #strong[Tracking the Cracking: a Holistic Analysis of Rapid Ice Shelf Fracture Using Seismology, Geodesy, and Satellite Imagery on the Pine Island Glacier Ice Shelf, West Antarctica]. Geophysical Research Letters, #link("https://doi.org/10.1029/2021GL097604")[10.1029\/2021GL097604]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Z. Yang], #emph[C. Yuan], #strong[M. A. Denolle] (2022). #strong[Detecting Elevated Pore Pressure due to Wastewater Injection Using Ambient Noise Monitoring]. The Seismic Record, 2, #link("https://doi.org/10.1785/0320210036")[10.1785\/0320210036]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], #strong[M. A. Denolle] (2021). #strong[The Earth's Surface Controls the Depth-Dependent Seismic Radiation of Megathrust Earthquakes]. AGU Advances, 2, #link("https://doi.org/10.1029/2021AV000413")[10.1029\/2021AV000413]

  ],
  [
    2021

  ],
  main-column-second-row: [
    Featured in: #link("https://eos.org/editor-highlights/the-highs-and-the-lows-of-megathrust-earthquakes")[EOS]

  ],
)

#regular-entry(
  [
    #emph[C. Yuan], #emph[J. Bryan], #strong[M. A. Denolle] (2021). #strong[Comparing approaches to measuring seismic phase variations in the time, frequency, and wavelet domains]. Geophysical Journal International, 226, #link("https://doi.org/10.1093/gji/ggab140")[10.1093\/gji\/ggab140]

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], Z. Li, #strong[M. A. Denolle] (2021). #strong[Source time function clustering reveals patterns in earthquake dynamics]. Seismological Research Letters, 92, #link("https://doi.org/10.1785/0220200403")[10.1785\/0220200403]

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Clements], #strong[M. A. Denolle] (2021). #strong[SeisNoise.jl: Ambient Seismic Noise Cross Correlation on the CPU and GPU in Julia]. Seismological Research Letters, 92, #link("https://doi.org/10.1785/0220200192")[10.1785\/0220200192]

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. A. Denolle], T. Nissen-Meyer (2020). #strong[Quiet Anthropocene, quiet Earth]. Science, 369, #link("https://doi.org/10.1126/science.abd8358")[10.1126\/science.abd8358]

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    J. P. Jones, #emph[K. Okubo], #emph[T. Clements], #strong[M. A. Denolle] (2020). #strong[SeisIO: A Fast, Efficient Geophysical Data Architecture for the Julia Language]. Seismological Research Letters, 91, #link("https://doi.org/10.1785/0220190295")[10.1785\/0220190295]

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[C. Jiang], #strong[M. A. Denolle] (2020). #strong[NoisePy: A new high-performance python tool for ambient-noise seismology]. Seismological Research Letters, 91, #link("https://doi.org/10.1785/0220190364")[10.1785\/0220190364]

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[P. Danré], #emph[J. Yin], B. Lipovsky, #strong[M. Denolle] (2019). #strong[Earthquakes Within Earthquakes: Patterns in Rupture Complexity]. Geophysical Research Letters, 43, #link("https://doi.org/10.1029/2019GL083093")[10.1029\/2019GL083093]

  ],
  [
    2019

  ],
  main-column-second-row: [
    Featured in: #link("https://news.harvard.edu/gazette/story/2019/08/early-seismic-waves-hold-the-clue-to-the-power-of-the-main-temblor/")[Harvard Gazette]

  ],
)

#regular-entry(
  [
    #emph[L. Viens], #strong[M. Denolle] (2019). #strong[Long-period ground motions from past and virtual megathrust earthquakes along the Nankai Trough, Japan]. Bulletin of the Seismological Society of America, 109, #link("https://doi.org/10.1785/0120180320")[10.1785\/0120180320]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle] (2019). #strong[Energetic Onset of Earthquakes]. Geophysical Research Letters, 46, #link("https://doi.org/10.1029/2018GL080687")[10.1029\/2018GL080687]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], #strong[M. Denolle] (2019). #strong[Relating teleseismic backprojection images to earthquake kinematics]. Geophysical Journal International, 217, #link("https://doi.org/10.1093/gji/ggz048")[10.1093\/gji\/ggz048]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    Y. Wang, #strong[M. Denolle], S. M. Day (2019). #strong[Geometric Controls on Pulse-like Rupture in a Dynamic Model of the 2015 Gorkha Earthquake]. Journal of Geophysical Research, 124, #link("https://doi.org/10.1029/2018JB016602")[10.1029\/2018JB016602]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Clements], #strong[M. Denolle] (2018). #strong[Tracking ground water using the ambient seismic field]. (User text suggests possible mismatch of volume\/issue) Geophysical Research Letters, 123, #link("https://doi.org/10.1029/2018GL077706")[10.1029\/2018GL077706]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Viens], #strong[M. Denolle], N. Hirata, S. Nakagawa (2018). #strong[Complex near-surface rheology inferred from the response of greater Tokyo to strong ground motions]. Journal of Geophysical Research: Solid Earth, 123

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. A. Denolle], P. Boué, N. Hirata, G. C. Beroza (2018). #strong[Strong Shaking Predicted in Tokyo From an Expected M7+ Itoigawa-Shizuoka Earthquake]. Journal of Geophysical Research: Solid Earth, 123

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[C. Van Houtte], #strong[M. Denolle] (2018). #strong[Improved model fitting for the empirical Green's function approach using hierarchical models]. Journal of Geophysical Research: Solid Earth, 123

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Clements], #strong[M. A. Denolle] (2018). #strong[Tracking groundwater levels using the ambient seismic field]. Geophysical Research Letters, 45, #link("https://doi.org/10.1029/2018GL077706")[10.1029\/2018GL077706]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Perol], M. Gharbi, #strong[M. Denolle] (2018). #strong[Convolutional neural network for earthquake detection and location]. Science Advances, 4

  ],
  [
    2018

  ],
  main-column-second-row: [
    Featured in: #link("https://news.harvard.edu/gazette/story/2018/03/researchers-create-algorithm-to-separate-earthquakes-from-seismic-noise/")[Harvard Gazette]

  ],
)

#regular-entry(
  [
    #emph[J. Yin], #strong[M. A. Denolle], H. Yao (2018). #strong[Spatial and Temporal Evolution of Earthquake Dynamics: Case Study of the Mw 8.3 Illapel Earthquake, Chile]. Journal of Geophysical Research: Solid Earth, 123, #link("https://doi.org/10.1002/2017JB014265")[10.1002\/2017JB014265]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    Y. Sheng, #strong[M. A. Denolle], G. C. Beroza (2017). #strong[Multicomponent C3 Green's Functions for Improved Long-Period Ground-Motion Prediction]. Bulletin of the Seismological Society of America, 107, #link("https://doi.org/10.1785/0120170053")[10.1785\/0120170053]

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Viens], #strong[M. Denolle], H. Miyake, S. Sakai, S. Nakagawa (2017). #strong[Retrieving impulse response function amplitudes from the ambient seismic field]. Geophysical Journal International, 210, #link("https://doi.org/10.1093/gji/ggx155")[10.1093\/gji\/ggx155]

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    P. Boue, #strong[M. Denolle], N. Hirata, S. Nakagawa, G. C. Beroza (2016). #strong[Beyond Basin Resonance: Characterizing Wave Propagation Using a Dense Array and the Ambient Seismic Field]. Geophysical Journal International, 206, #link("https://doi.org/10.1093/gji/ggw205")[10.1093\/gji\/ggw205]

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], P. M. Shearer (2016). #strong[New perspective on self-similarity of shallow thrust earthquakes]. Journal of Geophysical Research: Solid Earth, 121, #link("https://doi.org/10.1002/2016JB013105")[10.1002\/2016JB013105]

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], W. Fan, P. M. Shearer (2015). #strong[Dynamics of the M7.8 2015 Nepal Earthquake]. Geophysical Research Letters, 42, #link("https://doi.org/10.1002/2015GL065336")[10.1002\/2015GL065336]

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    E.-J. Lee, P. Chen, T. H. Jordan, P. B. Maechling, #strong[M. Denolle], G. C. Beroza (2014). #strong[Full 3D Tomography (F3DT) for Crustal Structure in Southern California Based on the Scattering-Integral (SI) and the Adjoint-Wavefield (AW) Methods]. Journal of Geophysical Research, 119, #link("https://doi.org/10.1002/2014JB011236")[10.1002\/2014JB011236]

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], H. Miyake, S. Nakagawa, N. Hirata, G. C. Beroza (2014). #strong[Long-period seismic amplification in the Kanto Basin from the ambient seismic field]. Geophysical Research Letters, 41, #link("https://doi.org/10.1002/2014GL059425")[10.1002\/2014GL059425]

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], E. M. Dunham, G. A. Prieto, G. C. Beroza (2014). #strong[Strong Ground Motion Prediction using Virtual Earthquakes]. Science, 343, #link("https://doi.org/10.1126/science.1245678")[10.1126\/science.1245678]

  ],
  [
    2014

  ],
  main-column-second-row: [
    Featured in: #link("https://www.youtube.com/watch?v=WTg3GzGCRfA")[Video]

  ],
)

#regular-entry(
  [
    #strong[M. Denolle], E. M. Dunham, G. A. Prieto, G. C. Beroza (2013). #strong[Ground Motion Prediction of Realistic Earthquake Sources Using the Ambient Seismic Field]. Journal of Geophysical Research, 118, #link("https://doi.org/10.1029/2012JB009603")[10.1029\/2012JB009603]

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    J. F. Lawrence, #strong[M. Denolle], K. J. Seats, G. Prieto (2013). #strong[A numeric evaluation of attenuation from ambient noise correlation functions]. Journal of Geophysical Research, 118, #link("https://doi.org/10.1002/2012JB009513")[10.1002\/2012JB009513]

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], E. M. Dunham, G. C. Beroza (2012). #strong[Solving the Surface-Wave Eigenproblem with Chebyshev Spectral Collocation]. Bulletin of the Seismological Society of America, 102, #link("https://doi.org/10.1785/0120110183")[10.1785\/0120110183]

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    G. A. Prieto, #strong[M. Denolle], J. F. Lawrence, G. C. Beroza (2011). #strong[On amplitude carried by the ambient seismic field]. Comptes Rendus Geoscience (Thematic Issue: Imaging and Monitoring with Seismic Noise), 343

  ],
  [
    2011

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    S. Singh, N. Hananto, A. Chauhan, H. Permana, #strong[M. Denolle], A. Hendriyana, D. Natawidjaja (2010). #strong[Evidence of active backthrusting at the NE Margin of Mentawai Islands, SW, Sumatra]. Geophysical Journal International, 180, #link("https://doi.org/10.1111/j.1365-246X.2009.04458.x")[10.1111\/j.1365-246X.2009.04458.x]

  ],
  [
    2010

  ],
  main-column-second-row: [
  ],
)

== Grants

#education-entry(
  [
    #strong[Jerry and Linda Paros] Mult-Sensor, Multi-Geohazards Monitoring at Mt Rainier and Mountaineous regions: \$750,000 (lead PI

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[UW CRESST - FFST] Toward Predictive Understanding of Climate-Compounded Geohazards: \$300,000 (lead PI

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF  CS4All] Separating the Signal from the Noise: Promoting Alaskan students inquiry with geographically relevant seismic data and machine learning techniques: \$889,766 (lead PI Lore, Denolle co-PI, \$62,000 to UW), DRL-2524060

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF RISE CAIG] Collaborative Research: CAIG: Framework for Artificial Intelligence-Enhanced Modeling of Wildfire Geohazards (FAIM-WG): Applications for postfire debris flows across the Western US: \$735,074 (lead PI Istanbulluoglu, Denolle co-PI), RISE-2530591

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF OCE] Multi-span distributed fiber sensing on the Ocean Observatories Initiative Regional Cabled Array: \$880,490 (lead PI Wilcock, Denolle co-PI), OCE-2526198, technology development grant.

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF OCE] EXTension on the ENDeavour Segment (EXTEND): Illuminating the seafloor spreading cycle: \$785,819.00 (lead PI Wilcock, Denolle co-PI), OCE-2439442

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF EAR] Collaborative Research: A seismic investigation of slow slip and fault locking along the Alaska-Aleutian subduction zone: \$248,835.00 (Denolle co-PI, collaborative with lead PI Golos), EAR-2346079

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF OCE] RAPID: Multiplexed Distributed Acoustic Sensing (DAS) at the Ocean Observatory Initiative (OOI) Regional Cabled Array (RCA): \$198,069.00 (lead PI Wilcock, Denolle co-PI), OCE-2415521

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Ecole Normal Supérieure de Paris] Travel Fellowship: \$3,500 (Denolle PI)

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SCEC] CyberTraining for Seismology: Data Science and HPC: \$35,229 (Denolle PI)

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[David and Lucile Packard Foundation] URG Program: \$50,000 (PI)

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Murdock Charitable Trust Fund] UW FiberLab equipment: \$950,000 (co-PI, lead PI Brad Lipovsky). Built facility for Fiber Sensing.

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF CyberTraining] GeoSMART ML workforce development: \$995,817 (co-PI). Build a course MLGEO.

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF OAC-CSSI] Collaborative Research: Frameworks: Seismic COmputational Platform for Empowering Discovery (SCOPED): \$717,441.00 (Denolle PI, lead-PI Carl Tape), OAC-2103701

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF EAR, PREEVENTS] Collaborative Research: Cross-Validation of Empirical and Physics-based ground motion predictions: \$167,804.00 (Denolle PI), EAR-2125337

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SCEC grant] Aftershock patterns and co-seismic off-fault damage elucidate dynamic rupture processes on the 2019 Ridgecrest earthquake sequence: \$33,307 (Denolle PI) - returned

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Harvard University - David Rockefeller Center for Latin American Studies] Monitoring Seismic Hazards in Mexico City using Grillo, a Low-Cost Earthquake Early Warning System, Hardware, \$85,000 (Denolle PI)

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Harvard Data Science Initiative] Ambient-noise seismology using Cloud Computing: \$27,210 (Denolle PI)

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF EAR, CAREER] CAREER: Dynamics of surface rupturing thrust earthquakes: \$504,315 (PI)

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SCEC grant] Data Collection for Virtual Earthquakes on Cajon Pass: \$28,085 (Denolle PI) - field work

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[David and Lucile Packard Foundation] Fellowship: \$875,000 (PI)

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[NSF PREEVENTS] Collaborative Proposal - PREEVENTS Track 2: Cascadia Scenario Earthquakes: Source, Path, and implications for Earthquake Early Warning: \$324,495.00 (Denolle PI, collaborative with lead PI Yihe Huang and Amanda Thomas), EAR-1739712

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SCEC grant] Static and dynamic source parameters of global strike-slip earthquakes: \$25,000 (Denolle PI)

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SCEC grant] Epistemic uncertainties in ground motion prediction from virtual earthquakes: \$26,173 (Denolle PI)

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SCEC grant] Basin Response to Virtual Earthquakes on the San Jacinto Fault and the Itoigawa-Shizuoka Fault: \$20,000 (Denolle PI)

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

== Research Products

#education-entry(
  [
    #strong[Machine Learning in the Geosciences (Open-Access Jupyter Book)] Textbook

  ],
  [
    2021 – present

  ],
  main-column-second-row: [
    #summary[#link("https://geo-smart.github.io/mlgeo-book/")[Book] and #link("https://github.com/geo-smart/mlgeo-book")[course repository] provide graduate-level ML curriculum, asynchronous modules, and homework data pipelines for geoscience training.]

    - Addresses a core gap: no canonical ML textbook existed for geoscience graduate classrooms.

    - Adoption and contribution interest from peer programs (including Arizona and Berkeley).

    - Ongoing community development with curated datasets and reproducible teaching workflows.

  ],
)

#education-entry(
  [
    #strong[NoisePy] Software

  ],
  [
    2019 – present

  ],
  main-column-second-row: [
    #summary[Open-source Python software for large-scale ambient-noise seismology. #link("https://github.com/noisepy/NoisePy")[GitHub].]

    - Community scale: 207 stars, 83 forks, 19 contributors (Jan 2026).

    - Operational usage: taught in workshops and used for large-scale cross-correlation workflows.

    - Open, version-controlled development supporting reproducible and cloud-oriented processing.

  ],
)

#education-entry(
  [
    #strong[SeisNoise.jl] Software

  ],
  [
    2020 – present

  ],
  main-column-second-row: [
    #summary[Open-source Julia software for high-performance ambient-noise processing and cross-correlation. #link("https://github.com/tclements/SeisNoise.jl/")[GitHub].]

    - Extends the Julia seismology ecosystem with core ambient-noise tooling.

    - Community signal: 50 stars and 17 forks (Apr 2023 snapshot).

    - Used by group members for production research workflows.

  ],
)

#education-entry(
  [
    #strong[EarthML4PNW \/ PNW AI-Ready Seismic Dataset] Dataset

  ],
  [
    2023

  ],
  main-column-second-row: [
    #summary[Curated ML-ready Pacific Northwest dataset product. #link("https://github.com/EarthML4PNW/PNW-ML")[Dataset repository].]

    - Publication link: Seismica (2023), DOI #link("https://doi.org/10.26443/seismica.v2i1.368")[10.26443\/seismica.v2i1.368].

    - Version-controlled release and metadata stewardship through GitHub workflows.

    - Designed for reproducible benchmarking and graduate-level ML coursework.

  ],
)

#education-entry(
  [
    #strong[Global Seismic Phase Database] Dataset

  ],
  [
    2025

  ],
  main-column-second-row: [
    #summary[Global seismic data product from cloud-scale waveform processing. #link("https://doi.org/10.26443/seismica.v4i2.1738")[DOI].]

    - Scale: 4.3 billion phase picks from 1.3 PB of continuous seismic data.

    - Publication link: Seismica (2025) with DOI-backed archival record.

    - Supports global monitoring and data-driven geophysics workflows.

  ],
)

== Invited Talks

#education-entry(
  [
    #strong[NGF Science Meeting] Conference Speaker

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[WCCM 2026, Munich] Conference Speaker

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[European Geophysical Union] Conference Speaker

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[CERI Memphis] Department Colloquium

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[SIAM Geoscience Meeting] Plenary Speaker

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Workshop on Earthquake Physics and Applications of AI to Tectonic Faulting, Italy] Plenary Speaker

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Civil Environmental Engineering, University of Washington] Department Colloquium

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Radcliffe Institute of Advanced Studies, on the road] Short Talk

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Washington University, Saint Louis] Department Colloquium

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Southern California] Department Colloquium

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of California, Davis] Department Colloquium

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Northern Arizona University] Department Colloquium

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Passive imaging and monitoring in wave physics (Cargese, France)] Invited Conference Talk

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Statewide California Earthquake Center] Plenary Speaker

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Ecole Normale Supérieure, Paris] Séminaire Departemental

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[eScience Institute, University of Washington] Data Science Seminar

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Sandia National Lab, GNEM seminar series] Department Colloquium

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[American Geophysical Union (x2)] Invited Conference Talk

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of New Mexico] Department Colloquium

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Oregon] Seismo Colloquium

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[U Utah, Seismo Tea] Seismo Colloquium

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Wisconsin] Department Colloquium

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Colorado School of Mines] Department Colloquium

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Mexico a traves de los sismos] Invited Conference Talk

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Washington] Department Colloquium

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[UC Berkeley] Department Colloquium

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Yale University] Department Colloquium

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Washington, seismolunch] Seismo Colloquium

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[EGU annual meeting, Vienna] Invited Conference Talk

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Michigan State University] Department Colloquium

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Victoria University of Wellington, SN Jepson Lecture, New Zealand] Public Lecture

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[GNS-Science, New Zealand] Department Colloquium

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Stanford University, Department of Geophysics] Department Colloquium

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Tufts University, Civil Engineering seminar] Department Colloquium

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Brown University] Department Colloquium

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Ecole Normale Superieure, Paris] Department Colloquium

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[AGU, New Orleans] Invited Conference Talk

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Columbia University, Lamont Doherty Earth Observatory] Department Colloquium

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Harvard Museum of Natural History] Public Lecture

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Oregon] Department Colloquium

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of New Hampshire, Chapman Colloquium] Department Colloquium

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[UC Santa Cruz, IGPP seminar] Department Colloquium

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Massachusetts Institute of Technology] Department Colloquium

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[USGS, Menlo Park, Earthquake Hazard Program] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Victoria, BC, Canada] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Penn State, Geodynamics seminar] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Harvard, Earth and Planetary Sciences] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[UT Austin, Solid Earth seminar] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[UCLA, seismology\/tectonics seminar] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[HOKUDAN International Symposium on Active Faulting, Awaji, Japan] Invited Conference Talk

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Information Theory and Applications workshop, La Jolla] Invited Conference Talk

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[IGPP-Scripps Institution of Oceanography, UCSD, Geophysics seminar] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[University of Southern California, Geophysics seminar] Department Colloquium

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Strong Motion Studies for Future Mega-Quakes, DPRI, Kyoto University, Japan] Invited Conference Talk

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[AGU-SEG Summer Research workshop, Vancouver, Canada] Invited Conference Talk

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[San Diego State University] Department Colloquium

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[UC Santa Barbara] Department Colloquium

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[IGPP-Scripps Institution of Oceanography, UCSD, Geophysics seminar] Department Colloquium

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[AGU, Meeting of the Americas, Cancun, Mexico] Invited Conference Talk

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Caltech Seismo Lab] Department Colloquium

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[USGS, Menlo Park] Department Colloquium

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Stanford ICME seminar] Department Colloquium

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Earthquake Research Institute, Tokyo University, Japan] Department Colloquium

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Advanced Industrial Science and Technology, Japan] Department Colloquium

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Disaster Prevention Research Institute, Japan] Department Colloquium

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[ACOUSTICS, France] Invited Conference Talk

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Berkeley Seismo Lab] Department Colloquium

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#education-entry(
  [
    #strong[Institut de Physique du Globe de Paris, Earthquake seminar] Department Colloquium

  ],
  [
    2011

  ],
  main-column-second-row: [
  ],
)
