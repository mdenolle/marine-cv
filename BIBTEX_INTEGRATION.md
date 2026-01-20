# Marine Denolle CV - BibTeX Integration

This directory contains tools for automatically generating the publications section of the CV from a BibTeX file.

## Quick Start

1. **Update publications in BibTeX**: Edit `marine-cv-docs/denolle-pub.bib`

2. **Regenerate publications YAML**:
   ```bash
   python scripts/generate_publications.py > marine-cv-docs/temp_publications.yaml
   ```

3. **Review and update main CV**: Copy the generated publications section into `Marine_Denolle_CV.yaml`

4. **Render CV**:
   ```bash
   rendercv render marine-cv-docs/Marine_Denolle_CV.yaml
   ```

## Files

- `marine-cv-docs/denolle-pub.bib` - BibTeX file with all publications
- `marine-cv-docs/Marine_Denolle_CV.yaml` - Main CV YAML file
- `src/rendercv/bibtex_parser.py` - BibTeX parser module
- `scripts/generate_publications.py` - Script to generate publications YAML

## Features

### Group Member Tagging

The parser automatically tags co-authors who are group members with an asterisk (*). Group members are defined in `bibtex_parser.py`:

- **PhD Students**: Yiyu Ni, Manuela Kopefli, Akash Kharita, Michael Hemmett, Congcong Yuan, Stephanie Olinger, Tim Clements, Jiuxun Yin
- **Postdocs**: Qibin Shi, Kuan-Fu Feng, Ethan Williams, Laura Ermert, Xiaotao Yang, Kurama Okubo, Zhitu Ma, Chengxin Jiang, Loïc Viens
- **Other mentees**: Pierre Danré, Jared Bryan, Julian Schmitt, Francesca Skene, Albert Aguilar, Chris Van Houtte, Thibaud Perol

### Media Coverage

Key publications with media coverage are linked automatically. Edit the `MEDIA_COVERAGE` dictionary in `scripts/generate_publications.py` to add/update links:

```python
MEDIA_COVERAGE = {
    'Denolle2014': [
        'https://news.stanford.edu/...',
    ],
    'Perol2018': [...],
    # ...
}
```

## Customization

### Adding a New Group Member

Edit `src/rendercv/bibtex_parser.py` and add the name to `DEFAULT_GROUP_MEMBERS`:

```python
DEFAULT_GROUP_MEMBERS = [
    'Yiyu Ni',
    'New Member Name',  # Add here
    # ...
]
```

### Adding Media Coverage

Edit `scripts/generate_publications.py` and add to `MEDIA_COVERAGE`:

```python
MEDIA_COVERAGE = {
    'CitationKey2025': [
        'https://news.example.com/article',
    ],
}
```

## Testing

Test the BibTeX parser:
```bash
python src/rendercv/bibtex_parser.py marine-cv-docs/denolle-pub.bib
```

Preview first 10 publications:
```bash
python scripts/generate_publications.py | head -100
```

## Schema

The CV uses a customized schema.json that supports:
- `university` field (alternative to `company` for academic positions)
- `media_coverage` field in publications (array of URLs)

## Troubleshooting

### "BibTeX file not found"
Make sure you run the script from the repository root directory.

### "Group members not tagged"
Check that names in `DEFAULT_GROUP_MEMBERS` match the author names in the BibTeX file (case-insensitive last name matching).

### "Media coverage not appearing"
Verify the citation key in `MEDIA_COVERAGE` matches the `@article{KEY,` in the .bib file.

## Advanced Usage

### Custom Group Member Lists

```python
from rendercv.bibtex_parser import bibtex_to_rendercv

publications = bibtex_to_rendercv(
    'denolle-pub.bib',
    group_members=['Custom Name 1', 'Custom Name 2'],
    media_coverage={'Key2025': ['url1', 'url2']}
)
```

### Extract Only Group Member Publications

```python
from rendercv.bibtex_parser import extract_group_member_publications

yaml_output = extract_group_member_publications(
    'denolle-pub.bib',
    group_members=['Yiyu Ni', 'Tim Clements'],
    output_format='yaml'
)
```

## Dependencies

- `bibtexparser>=1.4.1` - BibTeX parsing
- `pydantic>=2.10.6` - Data validation
- `ruamel.yaml>=0.18` - YAML processing
- `rendercv>=2.6` - CV rendering

Install all dependencies:
```bash
pixi install
# or
conda env create -f environment.yml
```
