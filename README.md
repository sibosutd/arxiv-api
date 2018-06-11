# arxiv-api

Python wrapper for arXiv API and some useful examples.

I am just tired of manually renaming the papers downloaded from arXiv..

## Dependencies
+ feedparser
+ requests

## Usage

### Useful Scripts

1. **Download PDF examples:**

    ```shell
    python download.py [-h] [--dir DIR] --id ID [--prepend] [--slugify]
    ```

2. **Rename PDF files in default format to paper titles:**

    ```shell
    python id2name.py [-h] [--dir DIR] [--prepend] [--slugify] [--log LOG]
    ```

    Sample logging messages:
    ```
    Renaming file in: ~/Downloads/arxiv_folder
    Ignoring file: Learning to Segment Every Thing.pdf
    Renaming file: 1805.08318.pdf to Self_Attention_Generative_Adversarial_Networks.pdf
    ```


### API Interface

+ API Usage

    ```python
    arxiv.query(search_query, id_list, prune, start, max_results, sort_by, sort_order)
    ```

    | **Argument**   | **Type**        | **Default**    | **Required?** |
    |----------------|-----------------|----------------|---------------|
    | `search_query` | string          | `""`           | No            |
    | `id_list`      | list of strings | `[]`           | No            |
    | `start`        | int             | 0              | No            |
    | `max_results`  | int             | 10             | No            |
    | `sort_by`      | string          | `"relevance"`  | No            |
    | `sort_order`   | string          | `"descending"` | No            |

    + `search_query` is a query string; details of its usage are documented [here](https://arxiv.org/help/api/user-manual#Quickstart).
    + `id_list` contains arXiv record IDs (typically of the format `"0710.5765v1"`)
    + `start` is the result offset for paging through a long query result. If set to 0, the API response will begin with the first result; if set to 10, the API response will begin with the 11th.
    + `max_results` is the maximum number of results per query.

    All of these arguments are documented more comprehensively in the [arXiv API documentation](https://arxiv.org/help/api/user-manual#Quickstart).

+ Optional Arguments

    | **Argument** | **Type** | **Default** | **Required?** |
    |--------------|----------|-------------|---------------|
    | `dir`        | string   | `"./"`      | No            |
    | `prepend`    | boolean  | False       | No            |
    | `slugify`    | boolean  | False       | No            |
    | `log`        | string   | "INFO"      | No            |

    + `dir` is the relative directory path to which the downloaded PDF will be saved. It defaults to the present working directory.
    + When `prepend` is True, the arXiv record ID will be prepended to the download filename.
    + When `slugify` is True, the paper title will be stripped of non-alphanumeric characters before being used as a filename.

## Reference

+ [lukasschwab/arxiv.py](https://github.com/lukasschwab/arxiv.py)
+ [Phyks/libbmc](https://github.com/Phyks/libbmc)
