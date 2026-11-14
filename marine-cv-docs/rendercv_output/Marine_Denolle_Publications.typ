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
    month: 11,
    day: 14,
  ),
)


= Marine A. Denolle

  #headline([Publications | Associate Professor, Earth and Space Sciences, University of Washington])

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
    #emph[Qibin Shi], David R. Montgomery, Abigail L.S. Swann, Nicoleta C. Cristea, #emph[Ethan F. Williams], Nan You, Simon Jeffery, Joe Collins, Ana Prada Barrio, Paula A. Misiewicz, Tarje Nissen-Meyer, #strong[Marine A. Denolle] (2026). #strong[Agroseismology and the impact of farming practices on soil hydrodynamics]. Science, 392(6795), 306–310, #link("https://doi.org/10.1126/science.aec0970")[10.1126\/science.aec0970]

  ],
  [
    2026

  ],
  main-column-second-row: [
    Featured in: #link("https://www.washington.edu/news/2026/03/19/earthquake-scientists-reveal-how-overplowing-weakens-soil-at-experimental-farm/")[UW News], #link("https://grist.org/drought/fiber-optic-cables-reveal-a-serious-problem-at-the-heart-of-modern-farming/")[Grist], #link("https://www.dailyuw.com/article/uw-study-on-soil-structure-helps-explain-the-why-in-plowing-debate-20260421")[Dailyuw]

  ],
)

#regular-entry(
  [
    #emph[Maleen Kidiwela], #strong[Marine A. Denolle], William S. D. Wilcock, #emph[Kuan-Fu Feng] (2026). #strong[Active protothrusts and fluid highways: Seismic noise reveals hidden subduction dynamics in Cascadia]. Science Advances, 12(9), eaea3684, #link("https://doi.org/10.1126/sciadv.aea3684")[10.1126\/sciadv.aea3684]

  ],
  [
    2026

  ],
  main-column-second-row: [
    Featured in: #link("https://www.npr.org/2026/03/05/nx-s1-5732773/this-week-in-science-prehistoric-cooking-earthquakes-in-the-pnw-and-teens-sleep?mkt_tok=MTMxLUFRTy0yMjUAAAGgcXIp-QXzGs0WlB22XUVMoYKPipJCRo8S4n33LPNaUafp1sPhgf2znlMDhypipbORq0-bRqsRe0CwLZW5j3bJrR_BVsSsoMwhzvCfexfE5HUYUjD5")[Npr], #link("https://www.washington.edu/news/2026/02/27/stress-testing-the-cascadia-subduction-zone-reveals-variability-that-could-impact-how-earthquakes-spread/")[UW News]

  ],
)

#regular-entry(
  [
    Han Xiao, Frederik Tilmann, Martijn van den Ende, Diane Rivet, Afonso Loureiro, Takeshi Tsuji, Arantza Ugalde, #emph[Qibin Shi], #strong[Marine A Denolle] (2026). #strong[DeepSubDAS: an earthquake phase picker from submarine distributed acoustic sensing data]. Geophysical Journal International, 245(2), ggag061, #link("https://doi.org/10.1093/gji/ggag061")[10.1093\/gji\/ggag061]

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Akash Kharita], #strong[Marine Denolle], Alexander Hutko, Renate Hartog, Stephen Malone (2026). #strong[Exploration of Machine Learning Methods to Seismic Event Discrimination in the Pacific Northwest]. Seismica, 5(1), #link("https://doi.org/10.26443/seismica.v5i1.2068")[10.26443\/seismica.v5i1.2068]

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    John Townend, Ilma del Carmen Juarez‐Garfias, Olivia Pita‐Sllim, Calum J. Chamberlain, Emily Warren‐Smith, Caroline Holden, Kasper van Wijk, #strong[Marine Denolle], Andrew Curtis, Hiroe Miyake (2026). #strong[Seismological Analysis of Contemporary and Future Alpine Fault Earthquakes Using the Southern Alps Long Skinny Array (SALSA)]. Seismological Research Letters, #link("https://doi.org/10.1785/0220250260")[10.1785\/0220250260]

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Natasha Toghramadjian], #strong[Marine A. Denolle], #emph[Laura Ermert], #emph[Chengxin Jiang] (2026). #strong[Probing the Seattle Basin Edge Using a Dense Urban Nodal Array in 100 Backyards]. Seismological Research Letters, 97(4), 2803–2816, #link("https://doi.org/10.1785/0220250241")[10.1785\/0220250241]

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
    #emph[Kuan-Fu Feng], #strong[Marine Denolle], Fan-Chi Lin, Tonie van Dam (2026). #strong[A Decadal Survey of the Near-Surface Seismic Velocity Response to Hydrological Variations in Utah, United States]. Journal of Geophysical Research: Solid Earth, 131(1), e2024JB030689, #link("https://doi.org/10.1029/2024JB030689")[10.1029\/2024JB030689]

  ],
  [
    2026

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Yiyu Ni], #strong[Marine Denolle], Amanda Thomas, Alex Hamilton, Jannes Münchmeyer, Yinzhi Wang, Loïc Bachelot, Chad Trabant, David Mencin (2025). #strong[A Global-scale Database of Seismic Phases from Cloud-based Picking at Petabyte Scale]. Seismica, 4(2), #link("https://doi.org/10.26443/seismica.v4i2.1738")[10.26443\/seismica.v4i2.1738]

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
    #emph[Yiyu Ni], #strong[Marine A Denolle], Jannes Münchmeyer, Yinzhi Wang, #emph[Kuan-Fu Feng], Carlos Garcia Jurado Suarez, Amanda M Thomas, Chad Trabant, Alex Hamilton, David Mencin (2025). #strong[A Review of Cloud Computing and Storage in Seismology]. Geophysical Journal International, 243(1), ggaf322, #link("https://doi.org/10.1093/gji/ggaf322")[10.1093\/gji\/ggaf322]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Marine A. Denolle], Carl Tape, Ebru Bozdağ, Yinzhi Wang, Felix Waldhauser, Alice‐Agnes Gabriel, Jochen Braunmiller, Bryant Chow, Liang Ding, #emph[Kuan‐Fu Feng], Ayon Ghosh, Nathan Groebner, Aakash Gupta, #emph[Zoe Krauss], Amanda M. McPherson, Masaru Nagaso, Zihua Niu, #emph[Yiyu Ni], Rıdvan Örsvuran, Gary Pavlis, Felix Rodriguez‐Cardozo, Theresa Sawi, David Schaff, Nico Schliwa, David Schneller, #emph[Qibin Shi], Julien Thurin, Chenxiao Wang, Kaiwen Wang, Jeremy Wing Ching Wong, Sebastian Wolf, #emph[Congcong Yuan] (2025). #strong[Training the Next Generation of Seismologists: Delivering Research‐Grade Software Education for Cloud and HPC Computing Through Diverse Training Modalities]. Seismological Research Letters, 96(5), 3265–3279, #link("https://doi.org/10.1785/0220240413")[10.1785\/0220240413]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[Marine A. Denolle], #emph[Qibin Shi], #emph[Tim Clements], #emph[Loïc Viens], Veronica Rodriguez-Tribaldos, Fabrice Cotton (2025). #strong[Ambient field seismology in critical zone hydrological sciences]. Comptes Rendus. Géoscience, 357(G1), 425–451, #link("https://doi.org/10.5802/crgeos.310")[10.5802\/crgeos.310]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Q. Shi], #strong[M. A. Denolle], #emph[Y. Ni], #emph[E. F. Williams], N. You (2025). #strong[Denoising Offshore Distributed Acoustic Sensing Using Masked Auto-Encoders to Enhance Earthquake Detection]. Journal of Geophysical Research: Solid Earth, 130(2), e2024JB029728, #link("https://doi.org/10.1029/2024JB029728")[10.1029\/2024JB029728]

  ],
  [
    2025

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Q. Shi], #emph[E. F. Williams], B. P. Lipovsky, #strong[M. A. Denolle], W. S. D. Wilcock, D. S. Kelley, K. Schoedl (2025). #strong[Multiplexed Distributed Acoustic Sensing Offshore Central Oregon]. Seismological Research Letters, 96(2A), 784–800, #link("https://doi.org/10.1785/0220240460")[10.1785\/0220240460]

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
    #emph[Y. Ni], #strong[M. A. Denolle], #emph[Q. Shi], B. P. Lipovsky, S. Pan, J. N. Kutz (2024). #strong[Wavefield reconstruction of distributed acoustic sensing: Lossy compression, wavefield separation, and edge computing]. Journal of Geophysical Research: Machine Learning and Computation, 1(3), e2024JH000247, #link("https://doi.org/10.1029/2024JH000247")[10.1029\/2024JH000247]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    P. Makus, #strong[M. A. Denolle], C. Sens-Schönfelder, #emph[M. Köpfli], F. Tilmann (2024). #strong[Analyzing Volcanic, Tectonic, and Environmental Influences on the Seismic Velocity from 25 Years of Data at Mount St. Helens]. Seismological Research Letters, 95(5), 2674–2688, #link("https://doi.org/10.1785/0220240088")[10.1785\/0220240088]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    M. Köpli, #strong[M. A. Denolle], W. Thelen, P. Makus, S. Malone (2024). #strong[Examining 22 Years of Ambient Seismic Wavefield at Mount St. Helens]. Seismological Research Letters, 95(5), 2622–2636, #link("https://doi.org/10.1785/0220240079")[10.1785\/0220240079]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    F. Diewald, #strong[M. Denolle], J. J. Timothy, C. Gehlen (2024). #strong[Impact of Temperature and Relative Humidity Variations on Coda Waves in Concrete]. Scientific Reports, 14(1), 18861, #link("https://doi.org/10.1038/s41598-024-69564-4")[10.1038\/s41598-024-69564-4]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[K. Okubo], B. Delbridge, #strong[M. Denolle] (2024). #strong[Monitoring velocity change over 20 years at Parkfield]. Journal of Geophysical Research: Solid Earth, 129(4), e2023JB028084, #link("https://doi.org/10.1029/2023JB028084")[10.1029\/2023JB028084]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[A. Kharita], #strong[M. Denolle], M. West (2024). #strong[Discrimination between icequakes and earthquakes in southern Alaska: an exploration of waveform features using random forest algorithm]. Geophysical Journal International, 237(2), 1189–1207, #link("https://doi.org/10.1093/gji/ggae106")[10.1093\/gji\/ggae106]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[S. Olinger], B. Lipovsky, #strong[M. Denolle] (2024). #strong[Ocean Coupling Limits Rupture Velocity of Fastest Observed Ice Shelf Rift Propagation Event]. AGU Advances, 5(1), e2023AV001023, #link("https://doi.org/10.1029/2023AV001023")[10.1029\/2023AV001023]

  ],
  [
    2024

  ],
  main-column-second-row: [
    Featured in: #link("https://www.washington.edu/news/2024/02/28/80-mph-speed-record-for-glacier-fracture-helps-reveal-the-physics-of-ice-sheet-collapse/")[UW News], #link("https://eos.org/editor-highlights/speed-of-ice-shelf-rifting-controlled-by-ocean-ice-interactions")[EOS]

  ],
)

#regular-entry(
  [
    #emph[C. Yuan], T. Cochard, #strong[M. Denolle], J. Gomberg, A. Wech, L. Xiao, D. Weitz (2024). #strong[Laboratory Hydrofractures as Analogs to Tectonic Tremors]. AGU Advances, 5(1), e2023AV001002, #link("https://doi.org/10.1029/2023AV001002")[10.1029\/2023AV001002]

  ],
  [
    2024

  ],
  main-column-second-row: [
    Featured in: #link("https://www.washington.edu/news/2024/01/29/qa-how-slow-slip-earthquakes-may-be-driven-by-deep-hydraulic-fracturing/")[UW News], #link("https://eos.org/research-spotlights/scientists-model-whats-moving-beneath-earths-surface")[EOS]

  ],
)

#regular-entry(
  [
    T. Cochard, I. Svetlizky, G. Albertini, R. C. Viesca, S. M. Rubinstein, F. Spaepen, #emph[C. Yuan], #strong[M. Denolle], Y.-Q. Song, L. Xiao, D. A. Weitz (2024). #strong[Propagation of extended fractures by local nucleation and rapid transverse expansion of crack-front distortion]. Nature Physics, 20(4), 660–665, #link("https://doi.org/10.1038/s41567-023-02365-0")[10.1038\/s41567-023-02365-0]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Yiyu Ni], #strong[Marine A. Denolle], Rob Fatland, Naomi Alterman, Bradley P. Lipovsky, Friedrich Knuth (2024). #strong[An Object Storage for Distributed Acoustic Sensing]. Seismological Research Letters, 95(1), 499–511, #link("https://doi.org/10.1785/0220230172")[10.1785\/0220230172]

  ],
  [
    2024

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Q. Shi], #strong[M. Denolle] (2023). #strong[Improved observations of deep earthquake ruptures using machine learning]. Journal of Geophysical Research: Solid Earth, 128(12), e2023JB027334, #link("https://doi.org/10.1029/2023JB027334")[10.1029\/2023JB027334]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Congcong Yuan], #emph[Yiyu Ni], Youzuo Lin, #strong[Marine Denolle] (2023). #strong[Better Together: Ensemble Learning for Earthquake Detection and Phase Picking]. IEEE Transactions on Geoscience and Remote Sensing, 61, 1–17, #link("https://doi.org/10.1109/TGRS.2023.3320148")[10.1109\/TGRS.2023.3320148]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Z. Krauss], #emph[Y. Ni], S. Henderson, #strong[M. Denolle] (2023). #strong[Seismology in the cloud: guidance for the individual researcher]. Seismica, 2(2), #link("https://doi.org/10.26443/seismica.v2i2.979")[10.26443\/seismica.v2i2.979]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Y. Ni], A. Hutko, #emph[F. Skene], #strong[M. Denolle], S. Malone, P. Bodin, R. Hartog, A. Wright (2023). #strong[Curated Pacific Northwest AI-ready Seismic Dataset]. Seismica, 2(1), #link("https://doi.org/10.26443/seismica.v2i1.368")[10.26443\/seismica.v2i1.368]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Ermert], E. Cabral-Cano, E. Chaussard, D. Solano-Rojas, L. Quintanar, D. Morales Padilla, E. A. Fernandez-Torres, #strong[M. A. Denolle] (2023). #strong[Probing environmental and tectonic changes underneath Mexico City with the urban seismic field]. Solid Earth, 14(5), 529–549, #link("https://doi.org/10.5194/se-14-529-2023")[10.5194\/se-14-529-2023]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Clements], #strong[M. A. Denolle] (2023). #strong[The Seismic Signature of California's Earthquakes, Droughts, and Floods]. Journal of Geophysical Research: Solid Earth, 128(1), e2022JB025553, #link("https://doi.org/10.1029/2022JB025553")[10.1029\/2022JB025553]

  ],
  [
    2023

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], #strong[M. A. Denolle], B. He (2022). #strong[A multitask encoder--decoder to separate earthquake and ambient noise signal in seismograms]. Geophysical Journal International, 231(3), 1806–1822, #link("https://doi.org/10.1093/gji/ggac290")[10.1093\/gji\/ggac290]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[C. Jiang], #strong[M. A. Denolle] (2022). #strong[Pronounced Seismic Anisotropy in Kanto Sedimentary Basin: A Case Study of Using Dense Arrays, Ambient Noise Seismology, and Multi-Modal Surface-Wave Imaging]. Journal of Geophysical Research: Solid Earth, 127(8), e2022JB024613, #link("https://doi.org/10.1029/2022JB024613")[10.1029\/2022JB024613]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Viens], #emph[C. Jiang], #strong[M. A. Denolle] (2022). #strong[Imaging the Kanto Basin seismic basement with earthquake and noise autocorrelation functions]. Geophysical Journal International, 230(2), 1080–1091, #link("https://doi.org/10.1093/gji/ggac101")[10.1093\/gji\/ggac101]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[S. D. Olinger], B. P. Lipovsky, #strong[M. A. Denolle], B. W. Crowell (2022). #strong[Tracking the Cracking: a Holistic Analysis of Rapid Ice Shelf Fracture Using Seismology, Geodesy, and Satellite Imagery on the Pine Island Glacier Ice Shelf, West Antarctica]. Geophysical Research Letters, 49(10), e2021GL097604, #link("https://doi.org/10.1029/2021GL097604")[10.1029\/2021GL097604]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[Z. Yang], #emph[C. Yuan], #strong[M. A. Denolle] (2022). #strong[Detecting Elevated Pore Pressure due to Wastewater Injection Using Ambient Noise Monitoring]. The Seismic Record, 2(1), 38–49, #link("https://doi.org/10.1785/0320210036")[10.1785\/0320210036]

  ],
  [
    2022

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], #strong[M. A. Denolle] (2021). #strong[The Earth's Surface Controls the Depth-Dependent Seismic Radiation of Megathrust Earthquakes]. AGU Advances, 2(3), e2021AV000413, #link("https://doi.org/10.1029/2021AV000413")[10.1029\/2021AV000413]

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
    #emph[C. Yuan], #emph[J. Bryan], #strong[M. A. Denolle] (2021). #strong[Numerical comparison of time-, frequency- and wavelet-domain methods for coda wave interferometry]. Geophysical Journal International, 226(2), 828–846, #link("https://doi.org/10.1093/gji/ggab140")[10.1093\/gji\/ggab140]

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], Z. Li, #strong[M. A. Denolle] (2021). #strong[Source time function clustering reveals patterns in earthquake dynamics]. Seismological Research Letters, 92(4), 2343–2353, #link("https://doi.org/10.1785/0220200403")[10.1785\/0220200403]

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Clements], #strong[M. A. Denolle] (2021). #strong[SeisNoise.jl: Ambient Seismic Noise Cross Correlation on the CPU and GPU in Julia]. Seismological Research Letters, 92(1), 517–527, #link("https://doi.org/10.1785/0220200192")[10.1785\/0220200192]

  ],
  [
    2021

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. A. Denolle], T. Nissen-Meyer (2020). #strong[Quiet Anthropocene, quiet Earth]. Science, 369(6509), 1299–1300, #link("https://doi.org/10.1126/science.abd8358")[10.1126\/science.abd8358]

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    J. P. Jones, #emph[K. Okubo], #emph[T. Clements], #strong[M. A. Denolle] (2020). #strong[SeisIO: A Fast, Efficient Geophysical Data Architecture for the Julia Language]. Seismological Research Letters, 91(4), 2368–2377, #link("https://doi.org/10.1785/0220190295")[10.1785\/0220190295]

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[C. Jiang], #strong[M. A. Denolle] (2020). #strong[NoisePy: A new high-performance python tool for ambient-noise seismology]. Seismological Research Letters, 91(3), 1853–1866, #link("https://doi.org/10.1785/0220190364")[10.1785\/0220190364]

  ],
  [
    2020

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[P. Danré], #emph[J. Yin], B. Lipovsky, #strong[M. Denolle] (2019). #strong[Earthquakes Within Earthquakes: Patterns in Rupture Complexity]. Geophysical Research Letters, 46(13), 7352–7360, #link("https://doi.org/10.1029/2019GL083093")[10.1029\/2019GL083093]

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
    #emph[L. Viens], #strong[M. Denolle] (2019). #strong[Long-period ground motions from past and virtual megathrust earthquakes along the Nankai Trough, Japan]. Bulletin of the Seismological Society of America, 109(4), 1312–1330, #link("https://doi.org/10.1785/0120180320")[10.1785\/0120180320]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle] (2019). #strong[Energetic Onset of Earthquakes]. Geophysical Research Letters, 46(5), 2458–2466, #link("https://doi.org/10.1029/2018GL080687")[10.1029\/2018GL080687]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[J. Yin], #strong[M. Denolle] (2019). #strong[Relating teleseismic backprojection images to earthquake kinematics]. Geophysical Journal International, 217(2), 729–747, #link("https://doi.org/10.1093/gji/ggz048")[10.1093\/gji\/ggz048]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    Y. Wang, #strong[M. Denolle], S. M. Day (2019). #strong[Geometric Controls on Pulse-like Rupture in a Dynamic Model of the 2015 Gorkha Earthquake]. Journal of Geophysical Research: Solid Earth, 124(2), 1544–1568, #link("https://doi.org/10.1029/2018JB016602")[10.1029\/2018JB016602]

  ],
  [
    2019

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Viens], #strong[M. Denolle], N. Hirata, S. Nakagawa (2018). #strong[Complex near-surface rheology inferred from the response of greater Tokyo to strong ground motions]. Journal of Geophysical Research: Solid Earth, 123(7), 5710–5729, #link("https://doi.org/10.1029/2018JB015697")[10.1029\/2018JB015697]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. A. Denolle], P. Boué, N. Hirata, G. C. Beroza (2018). #strong[Strong Shaking Predicted in Tokyo From an Expected M7+ Itoigawa-Shizuoka Earthquake]. Journal of Geophysical Research: Solid Earth, 123(5), 3968–3992, #link("https://doi.org/10.1029/2017JB015184")[10.1029\/2017JB015184]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[C. Van Houtte], #strong[M. Denolle] (2018). #strong[Improved model fitting for the empirical Green's function approach using hierarchical models]. Journal of Geophysical Research: Solid Earth, 123(4), 2923–2942, #link("https://doi.org/10.1002/2017JB014943")[10.1002\/2017JB014943]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Clements], #strong[M. A. Denolle] (2018). #strong[Tracking groundwater levels using the ambient seismic field]. Geophysical Research Letters, 45(13), 6459–6465, #link("https://doi.org/10.1029/2018GL077706")[10.1029\/2018GL077706]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[T. Perol], M. Gharbi, #strong[M. Denolle] (2018). #strong[Convolutional neural network for earthquake detection and location]. Science Advances, 4(2), e1700578, #link("https://doi.org/10.1126/sciadv.1700578")[10.1126\/sciadv.1700578]

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
    #emph[J. Yin], #strong[M. A. Denolle], H. Yao (2018). #strong[Spatial and Temporal Evolution of Earthquake Dynamics: Case Study of the Mw 8.3 Illapel Earthquake, Chile]. Journal of Geophysical Research: Solid Earth, 123(1), 344–367, #link("https://doi.org/10.1002/2017JB014265")[10.1002\/2017JB014265]

  ],
  [
    2018

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    Y. Sheng, #strong[M. A. Denolle], G. C. Beroza (2017). #strong[Multicomponent C3 Green's Functions for Improved Long-Period Ground-Motion Prediction]. Bulletin of the Seismological Society of America, 107(6), 2836–2845, #link("https://doi.org/10.1785/0120170053")[10.1785\/0120170053]

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #emph[L. Viens], #strong[M. Denolle], H. Miyake, S. Sakai, S. Nakagawa (2017). #strong[Retrieving impulse response function amplitudes from the ambient seismic field]. Geophysical Journal International, 210(1), 210–222, #link("https://doi.org/10.1093/gji/ggx155")[10.1093\/gji\/ggx155]

  ],
  [
    2017

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    P. Boue, #strong[M. Denolle], N. Hirata, S. Nakagawa, G. C. Beroza (2016). #strong[Beyond Basin Resonance: Characterizing Wave Propagation Using a Dense Array and the Ambient Seismic Field]. Geophysical Journal International, 206(2), 1261–1272, #link("https://doi.org/10.1093/gji/ggw205")[10.1093\/gji\/ggw205]

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], P. M. Shearer (2016). #strong[New perspectives on self-similarity for shallow thrust earthquakes]. Journal of Geophysical Research: Solid Earth, 121(9), 6533–6565, #link("https://doi.org/10.1002/2016JB013105")[10.1002\/2016JB013105]

  ],
  [
    2016

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], W. Fan, P. M. Shearer (2015). #strong[Dynamics of the 2015 M7.8 Nepal earthquake]. Geophysical Research Letters, 42(18), 7467–7475, #link("https://doi.org/10.1002/2015GL065336")[10.1002\/2015GL065336]

  ],
  [
    2015

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    E.-J. Lee, P. Chen, T. H. Jordan, P. B. Maechling, #strong[M. Denolle], G. C. Beroza (2014). #strong[Full-3-D tomography for crustal structure in Southern California based on the scattering-integral and the adjoint-wavefield methods]. Journal of Geophysical Research: Solid Earth, 119(8), 6421–6451, #link("https://doi.org/10.1002/2014JB011346")[10.1002\/2014JB011346]

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], H. Miyake, S. Nakagawa, N. Hirata, G. C. Beroza (2014). #strong[Long-period seismic amplification in the Kanto Basin from the ambient seismic field]. Geophysical Research Letters, 41(7), 2319–2325, #link("https://doi.org/10.1002/2014GL059425")[10.1002\/2014GL059425]

  ],
  [
    2014

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], E. M. Dunham, G. A. Prieto, G. C. Beroza (2014). #strong[Strong Ground Motion Prediction using Virtual Earthquakes]. Science, 343(6169), 399–403, #link("https://doi.org/10.1126/science.1245678")[10.1126\/science.1245678]

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
    #strong[M. Denolle], E. M. Dunham, G. A. Prieto, G. C. Beroza (2013). #strong[Ground Motion Prediction of Realistic Earthquake Sources Using the Ambient Seismic Field]. Journal of Geophysical Research: Solid Earth, 118(5), 2102–2118, #link("https://doi.org/10.1029/2012JB009603")[10.1029\/2012JB009603]

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    J. F. Lawrence, #strong[M. Denolle], K. J. Seats, G. Prieto (2013). #strong[A numeric evaluation of attenuation from ambient noise correlation functions]. Journal of Geophysical Research: Solid Earth, 118(12), 6134–6145, #link("https://doi.org/10.1002/2012JB009513")[10.1002\/2012JB009513]

  ],
  [
    2013

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    #strong[M. Denolle], E. M. Dunham, G. C. Beroza (2012). #strong[Solving the Surface-Wave Eigenproblem with Chebyshev Spectral Collocation]. Bulletin of the Seismological Society of America, 102(3), 1214–1223, #link("https://doi.org/10.1785/0120110183")[10.1785\/0120110183]

  ],
  [
    2012

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    G. A. Prieto, #strong[M. Denolle], J. F. Lawrence, G. C. Beroza (2011). #strong[On amplitude information carried by the ambient seismic field]. Comptes Rendus. Géoscience (Thematic Issue: Imaging and Monitoring with Seismic Noise), 343(8-9), 600–614, #link("https://doi.org/10.1016/j.crte.2011.03.006")[10.1016\/j.crte.2011.03.006]

  ],
  [
    2011

  ],
  main-column-second-row: [
  ],
)

#regular-entry(
  [
    S. Singh, N. Hananto, A. Chauhan, H. Permana, #strong[M. Denolle], A. Hendriyana, D. Natawidjaja (2010). #strong[Evidence of active backthrusting at the NE Margin of Mentawai Islands, SW, Sumatra]. Geophysical Journal International, 180(2), 703–714, #link("https://doi.org/10.1111/j.1365-246X.2009.04458.x")[10.1111\/j.1365-246X.2009.04458.x]

  ],
  [
    2010

  ],
  main-column-second-row: [
  ],
)
