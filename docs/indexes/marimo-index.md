# Marimo Documentation & Example Index

Navigation map for the marimo documentation set and accompanying runnable notebooks. Each entry lists the relative path (from docs/indexes/), a concise summary, and related examples where applicable.

## Getting Started & Core Reference

[../marimo/docs/index.md](../marimo/docs/index.md)
- Summary: High-level introduction to marimo’s reactive notebooks, install snippets, highlight videos, and quickstart pointers.
- Examples: ../marimo/docs/apps/intro.py, ../marimo/examples/layouts/grid-dashboard.py, ../marimo/examples/ui/layout.py

[../marimo/docs/getting_started/index.md](../marimo/docs/getting_started/index.md)
- Summary: Landing page linking installation, quickstart, and key concepts tutorials for first-time users.
- Examples: ../marimo/examples/README.md

[../marimo/docs/getting_started/installation.md](../marimo/docs/getting_started/installation.md)
- Summary: Environment setup guidance plus pip/uv/conda instructions, recommended extras, and verification steps.
- Examples: None

[../marimo/docs/getting_started/quickstart.md](../marimo/docs/getting_started/quickstart.md)
- Summary: Walkthrough of marimo tutorial, edit, run, convert, and export workflows with optional AI/formatter setup.
- Examples: ../marimo/examples/running_as_a_script/with_argparse.py, ../marimo/examples/layouts/grid-dashboard.py

[../marimo/docs/getting_started/key_concepts.md](../marimo/docs/getting_started/key_concepts.md)
- Summary: Explains reactive execution, markdown outputs, UI binding, SQL support, and package management basics.
- Examples: ../marimo/examples/ui/slider.py, ../marimo/examples/outputs/plots.py

[../marimo/docs/faq.md](../marimo/docs/faq.md)
- Summary: Answers common questions on Jupyter differences, hidden state elimination, widget behavior, and performance.
- Examples: ../marimo/examples/running_cells/multiple_definitions.py, ../marimo/examples/control_flow/stop_execution.py

[../marimo/docs/community.md](../marimo/docs/community.md)
- Summary: Lists community channels (GitHub, Discord, socials) and provides HTML/Markdown badges for marimo apps.
- Examples: None

[../marimo/docs/reading.md](../marimo/docs/reading.md)
- Summary: Curated blog posts, launch write-ups, and YouTube playlists explaining marimo’s design motivations.
- Examples: None

[../marimo/docs/recipes.md](../marimo/docs/recipes.md)
- Summary: “Recipe” snippets for timers, conditional outputs, forms, arrays/dicts, and button handling to drop into notebooks.
- Examples: ../marimo/examples/ui/batch_and_form.py, ../marimo/examples/ui/refresh.py

[../marimo/docs/cli.md](../marimo/docs/cli.md)
- Summary: Auto-generated reference for the marimo CLI (commands like edit, run, check, export).
- Examples: ../marimo/examples/running_as_a_script/textual_app.py

## Guides – Fundamentals & Workflows

[../marimo/docs/guides/index.md](../marimo/docs/guides/index.md)
- Summary: Master guide index linking reactivity, interactivity, data, AI, publishing, deployment, and more.
- Examples: ../marimo/docs/examples/index.md

[../marimo/docs/guides/reactivity.md](../marimo/docs/guides/reactivity.md)
- Summary: Deep dive into reactive DAG execution, mutation caveats, stale cells, and visualization tools.
- Examples: ../marimo/examples/running_cells/basics.py, ../marimo/examples/running_cells/in_memory_cache.py

[../marimo/docs/guides/interactivity.md](../marimo/docs/guides/interactivity.md)
- Summary: Explains mo.ui elements, composite controls, and how interactions trigger dependent cells.
- Examples: ../marimo/examples/ui/README.md, ../marimo/examples/ui/array_element.py

[../marimo/docs/guides/outputs.md](../marimo/docs/guides/outputs.md)
- Summary: Covers markdown editors, embedding values, media helpers, progress indicators, and layout utilities.
- Examples: ../marimo/examples/outputs/showing_multiple_outputs.py, ../marimo/examples/markdown/dynamic_markdown.py

[../marimo/docs/guides/state.md](../marimo/docs/guides/state.md)
- Summary: Advanced primer on mo.state, synchronizing elements, avoiding cycles, and when to prefer pure UI reactivity.
- Examples: ../marimo/examples/misc/task_list.py, ../marimo/examples/ui/batch_and_form.py

[../marimo/docs/guides/apps.md](../marimo/docs/guides/apps.md)
- Summary: Shows marimo run, app preview, drag-and-drop grid layouts, slides mode, and sharing layout metadata.
- Examples: ../marimo/examples/layouts/grid-dashboard.py, ../marimo/examples/layouts/slides.py

[../marimo/docs/guides/scripts.md](../marimo/docs/guides/scripts.md)
- Summary: Demonstrates running notebooks as scripts, parsing CLI args, and exporting outputs headlessly.
- Examples: ../marimo/examples/running_as_a_script/sharing_arguments.py, ../marimo/examples/running_as_a_script/with_simple_parsing.py

[../marimo/docs/guides/reusing_functions.md](../marimo/docs/guides/reusing_functions.md)
- Summary: Details promoting cells to top-level functions/classes via setup cells for reuse across projects.
- Examples: ../marimo/examples/misc/custom_configuration.py

[../marimo/docs/guides/best_practices.md](../marimo/docs/guides/best_practices.md)
- Summary: Recommendations on structuring notebooks, minimizing globals, sharing apps, and collaborating effectively.
- Examples: ../marimo/examples/misc/explore_your_own_data.py

[../marimo/docs/guides/expensive_notebooks.md](../marimo/docs/guides/expensive_notebooks.md)
- Summary: Techniques for gating expensive cells with mo.stop, lazy runtime configuration, and memory management.
- Examples: ../marimo/examples/running_cells/persistent_cache.py, ../marimo/examples/running_cells/in_memory_cache.py

[../marimo/docs/guides/island_example.md](../marimo/docs/guides/island_example.md)
- Summary: Example architecture isolating UI interactions (islands) to keep notebooks responsive.
- Examples: ../marimo/examples/misc/public_folder.py

[../marimo/docs/guides/exporting.md](../marimo/docs/guides/exporting.md)
- Summary: Step-by-step instructions for exporting notebooks to HTML and other formats from the UI or CLI.
- Examples: ../marimo/examples/running_as_a_script/textual_app.py

## Coming From Other Tools

[../marimo/docs/guides/coming_from/index.md](../marimo/docs/guides/coming_from/index.md)
- Summary: Hub for transition guides from Jupyter, Streamlit, Papermill, and Jupytext.
- Examples: ../marimo/examples/control_flow/stop_execution.py

[../marimo/docs/guides/coming_from/jupyter.md](../marimo/docs/guides/coming_from/jupyter.md)
- Summary: Migration tips for Jupyter users covering reactive execution, globals, and UI composition.
- Examples: ../marimo/examples/running_cells/multiple_definitions.py

[../marimo/docs/guides/coming_from/streamlit.md](../marimo/docs/guides/coming_from/streamlit.md)
- Summary: Shows how reactive UI replaces Streamlit callbacks and how to map layout primitives.
- Examples: ../marimo/examples/layouts/grid-dashboard.py

[../marimo/docs/guides/coming_from/jupytext.md](../marimo/docs/guides/coming_from/jupytext.md)
- Summary: Discusses pure-Python storage versus Jupytext notebooks and synchronization trade-offs.
- Examples: ../marimo/examples/README.md

[../marimo/docs/guides/coming_from/papermill.md](../marimo/docs/guides/coming_from/papermill.md)
- Summary: Suggests marimo scripting over Papermill pipelines and highlights parameterization options.
- Examples: ../marimo/examples/running_as_a_script/sharing_arguments.py

## Additional Fundamentals

[../marimo/docs/guides/molab.md](../marimo/docs/guides/molab.md)
- Summary: Introduces molab, marimo’s hosted environment for shareable notebook links.
- Examples: None

[../marimo/docs/guides/wasm.md](../marimo/docs/guides/wasm.md)
- Summary: Explains running notebooks via WebAssembly in the browser or self-hosted playgrounds.
- Examples: ../marimo/examples/cloud/README.md

[../marimo/docs/guides/debugging.md](../marimo/docs/guides/debugging.md)
- Summary: Interactive debugging via pdb, debugpy, AI assistance, and console logs.
- Examples: ../marimo/examples/running_cells/debugging.py

[../marimo/docs/guides/troubleshooting.md](../marimo/docs/guides/troubleshooting.md)
- Summary: Troubleshooting checklist for environment conflicts, autorun, and rendering issues.
- Examples: ../marimo/examples/misc/custom_configuration.py

## Guides – Configuration & Editor Features

[../marimo/docs/guides/configuration/index.md](../marimo/docs/guides/configuration/index.md)
- Summary: Catalog of runtime, theming, HTML head, and snippet configuration options.
- Examples: ../marimo/examples/misc/custom_configuration.py

[../marimo/docs/guides/configuration/runtime_configuration.md](../marimo/docs/guides/configuration/runtime_configuration.md)
- Summary: Autorun toggles, lazy execution, module reload, and other runtime behaviors.
- Examples: ../marimo/examples/running_cells/in_memory_cache.py, ../marimo/examples/ui/refresh.py

[../marimo/docs/guides/configuration/theming.md](../marimo/docs/guides/configuration/theming.md)
- Summary: Custom themes and fonts plus CSS injection tips.
- Examples: ../marimo/docs/stylesheets/extra.css

[../marimo/docs/guides/configuration/html_head.md](../marimo/docs/guides/configuration/html_head.md)
- Summary: Injecting head scripts/styles and managing public assets.
- Examples: ../marimo/examples/misc/public_folder.py

[../marimo/docs/guides/configuration/snippets.md](../marimo/docs/guides/configuration/snippets.md)
- Summary: Managing reusable snippets across notebooks.
- Examples: None

[../marimo/docs/guides/editor_features/index.md](../marimo/docs/guides/editor_features/index.md)
- Summary: Overview of the browser IDE—panels, LSP, Copilot, data explorer, dependency graph.
- Examples: ../marimo/examples/misc/explore_your_own_data.py

[../marimo/docs/guides/editor_features/overview.md](../marimo/docs/guides/editor_features/overview.md)
- Summary: Command mode, vim keys, editor settings, and workspace layout.
- Examples: None

[../marimo/docs/guides/editor_features/dataflow.md](../marimo/docs/guides/editor_features/dataflow.md)
- Summary: Dependency explorer and reactive highlighting walkthrough.
- Examples: ../marimo/examples/running_cells/debugging.py

[../marimo/docs/guides/editor_features/package_management.md](../marimo/docs/guides/editor_features/package_management.md)
- Summary: Sandbox installs, inline requirements, and dependency graph integration.
- Examples: None

[../marimo/docs/guides/editor_features/ai_completion.md](../marimo/docs/guides/editor_features/ai_completion.md)
- Summary: AI assistant, Copilot integration, and custom prompts.
- Examples: ../marimo/examples/ai/chat/openai_example.py

[../marimo/docs/guides/editor_features/language_server.md](../marimo/docs/guides/editor_features/language_server.md)
- Summary: LSP diagnostics, code intelligence, and completions support.
- Examples: None

[../marimo/docs/guides/editor_features/hotkeys.md](../marimo/docs/guides/editor_features/hotkeys.md)
- Summary: Shortcut cheat sheet for notebook editing and execution.
- Examples: None

[../marimo/docs/guides/editor_features/module_autoreloading.md](../marimo/docs/guides/editor_features/module_autoreloading.md)
- Summary: Module reload behavior, caveats, and recommended workflows.
- Examples: ../marimo/examples/ui/refresh.py

[../marimo/docs/guides/editor_features/agents.md](../marimo/docs/guides/editor_features/agents.md)
- Summary: Editor AI agents usage, tool integrations, and prompt patterns.
- Examples: ../marimo/examples/ai/tools/chat_with_tools.py

[../marimo/docs/guides/editor_features/watching.md](../marimo/docs/guides/editor_features/watching.md)
- Summary: Editing notebooks from external editors with live reloading.
- Examples: None

## Guides – Data, Packages, AI

[../marimo/docs/guides/working_with_data/index.md](../marimo/docs/guides/working_with_data/index.md)
- Summary: Entry point to dataframes, SQL cells, and plotting guidance.
- Examples: ../marimo/examples/sql/querying_dataframes.py, ../marimo/examples/ui/dataframe.py

[../marimo/docs/guides/working_with_data/dataframes.md](../marimo/docs/guides/working_with_data/dataframes.md)
- Summary: Interactive dataframe tooling, transformations, and display controls.
- Examples: ../marimo/examples/outputs/dataframes.py

[../marimo/docs/guides/working_with_data/sql.md](../marimo/docs/guides/working_with_data/sql.md)
- Summary: DuckDB SQL cells, external connections, and parameterization.
- Examples: ../marimo/examples/sql/connect_to_postgres.py

[../marimo/docs/guides/working_with_data/plotting.md](../marimo/docs/guides/working_with_data/plotting.md)
- Summary: Altair, Plotly, matplotlib, and other visualization integrations.
- Examples: ../marimo/examples/outputs/plots.py

[../marimo/docs/guides/generate_with_ai/index.md](../marimo/docs/guides/generate_with_ai/index.md)
- Summary: AI entry page pointing to zero-shot notebooks and prompt collections.
- Examples: ../marimo/examples/ai/README.md

[../marimo/docs/guides/generate_with_ai/text_to_notebook.md](../marimo/docs/guides/generate_with_ai/text_to_notebook.md)
- Summary: Shows how to generate complete notebooks from prompts with the `marimo new` CLI and longer prompt files.
- Examples: ../marimo/examples/ai/misc/pdf_question_answer.py

[../marimo/docs/guides/generate_with_ai/prompts.md](../marimo/docs/guides/generate_with_ai/prompts.md)
- Summary: Shares prompt templates for Claude Code setup and anywidget-based custom UI generation.
- Examples: ../marimo/examples/ai/data/model_comparison.py

[../marimo/docs/guides/package_management/index.md](../marimo/docs/guides/package_management/index.md)
- Summary: Best practices for inline dependencies, uv workflows, and project structure.
- Examples: ../marimo/examples/misc/custom_configuration.py

[../marimo/docs/guides/package_management/installing_packages.md](../marimo/docs/guides/package_management/installing_packages.md)
- Summary: Installing dependencies per notebook using pip, uv, or conda.
- Examples: None

[../marimo/docs/guides/package_management/importing_packages.md](../marimo/docs/guides/package_management/importing_packages.md)
- Summary: Managing imports with setup cells and best practices for reactivity.
- Examples: None

[../marimo/docs/guides/package_management/using_uv.md](../marimo/docs/guides/package_management/using_uv.md)
- Summary: Running notebooks with uvx ... --sandbox and managing uv environments.
- Examples: None

[../marimo/docs/guides/package_management/notebooks_in_projects.md](../marimo/docs/guides/package_management/notebooks_in_projects.md)
- Summary: Integrating marimo notebooks inside larger Python projects.
- Examples: None

[../marimo/docs/guides/package_management/inlining_dependencies.md](../marimo/docs/guides/package_management/inlining_dependencies.md)
- Summary: Embedding dependency metadata directly into notebooks.
- Examples: None

## Guides – Publishing, Deployment, Testing, Errors

[../marimo/docs/guides/publishing/index.md](../marimo/docs/guides/publishing/index.md)
- Summary: Publishing options including GitHub Pages, Cloudflare, Quarto, and embeddings.
- Examples: ../marimo/examples/cloud/modal/modal_app.py

**Sub-guides under publishing:**
- ../marimo/docs/guides/publishing/deploy.md – Explains edit vs run server deployments and links to the broader deployment guide.
- ../marimo/docs/guides/publishing/embedding.md – Embed apps inside other sites.
- ../marimo/docs/guides/publishing/github_pages.md – Deploy via GitHub Pages.
- ../marimo/docs/guides/publishing/mkdocs.md – Publish to MkDocs deployments.
- ../marimo/docs/guides/publishing/quarto.md – Export to Quarto projects.
- ../marimo/docs/guides/publishing/from_code_snippets.md – Convert code snippets into marimo apps.
- ../marimo/docs/guides/publishing/from_github.md – Publish notebooks pulled from GitHub repos.
- ../marimo/docs/guides/publishing/view_outputs_on_github.md – Render outputs within GitHub.
- ../marimo/docs/guides/publishing/playground.md – Launch the interactive marimo playground.
- ../marimo/docs/guides/publishing/cloudflare.md – Deploy via Cloudflare Workers/Pages.
- ../marimo/docs/guides/publishing/self_host_wasm.md – Host WASM builds yourself.
- ../marimo/docs/guides/publishing/community_cloud/index.md – Community cloud onboarding guide.

[../marimo/docs/guides/deploying/index.md](../marimo/docs/guides/deploying/index.md)
- Summary: Deployment catalogue—Docker, Nginx, Hugging Face, Railway, Ploomber, Modal, auth, scheduling, programmatic hosting.
- Examples: ../marimo/examples/cloud/modal/modal_app.py, ../marimo/examples/frameworks/fastapi/main.py

**Sub-guides under deploying:**
- ../marimo/docs/guides/deploying/deploying_docker.md
- ../marimo/docs/guides/deploying/deploying_nginx.md
- ../marimo/docs/guides/deploying/deploying_hugging_face.md
- ../marimo/docs/guides/deploying/deploying_railway.md
- ../marimo/docs/guides/deploying/deploying_ploomber.md
- ../marimo/docs/guides/deploying/prebuilt_containers.md
- ../marimo/docs/guides/deploying/deploying_public_gallery.md
- ../marimo/docs/guides/deploying/scheduled.md
- ../marimo/docs/guides/deploying/programmatically.md
- ../marimo/docs/guides/deploying/authentication.md

[../marimo/docs/guides/testing/index.md](../marimo/docs/guides/testing/index.md)
- Summary: Strategies for pytest, doctest, and CI integration.
- Examples: ../marimo/examples/testing/test_with_pytest.py, ../marimo/examples/testing/running_doctests.py
- ../marimo/docs/guides/testing/pytest.md – Specific pytest harness instructions.
- ../marimo/docs/guides/testing/doctest.md – Running doctests inside marimo notebooks.

[../marimo/docs/guides/debugging.md](../marimo/docs/guides/debugging.md)
- Summary: Interactive debugging via pdb, debugpy, AI assistance, and console logs.
- Examples: ../marimo/examples/running_cells/debugging.py

[../marimo/docs/guides/troubleshooting.md](../marimo/docs/guides/troubleshooting.md)
- Summary: Troubleshooting checklist for environment conflicts, autorun, and rendering issues.
- Examples: ../marimo/examples/misc/custom_configuration.py

[../marimo/docs/guides/understanding_errors/index.md](../marimo/docs/guides/understanding_errors/index.md)
- Summary: Explains marimo’s constraints (single definitions, no cycles, no import *, setup cell rules) and lint integration.
- Examples: ../marimo/examples/running_cells/multiple_definitions.py

**Sub-guides under understanding_errors:**
- ../marimo/docs/guides/understanding_errors/multiple_definitions.md
- ../marimo/docs/guides/understanding_errors/cycles.md
- ../marimo/docs/guides/understanding_errors/import_star.md
- ../marimo/docs/guides/understanding_errors/setup.md

[../marimo/docs/guides/lint_rules/index.md](../marimo/docs/guides/lint_rules/index.md)
- Summary: Linter overview with severity table and CLI usage.
- Examples: ../marimo/examples/running_cells/multiple_definitions.py

**Rule documents:**
- ../marimo/docs/guides/lint_rules/rules/unparsable_cells.md
- ../marimo/docs/guides/lint_rules/rules/multiple_definitions.md
- ../marimo/docs/guides/lint_rules/rules/cycle_dependencies.md
- ../marimo/docs/guides/lint_rules/rules/setup_cell_dependencies.md
- ../marimo/docs/guides/lint_rules/rules/invalid_syntax.md
- ../marimo/docs/guides/lint_rules/rules/general_formatting.md
- ../marimo/docs/guides/lint_rules/rules/parse_stdout.md
- ../marimo/docs/guides/lint_rules/rules/parse_stderr.md
- ../marimo/docs/guides/lint_rules/rules/empty_cells.md

## Guides – Integrations

[../marimo/docs/guides/integrating_with_marimo/index.md](../marimo/docs/guides/integrating_with_marimo/index.md)
- Summary: Overview of integrating third-party objects and custom UI into marimo.
- Examples: ../marimo/examples/third_party/README.md
- ../marimo/docs/guides/integrating_with_marimo/displaying_objects.md – Rendering arbitrary Python objects.
- Examples: None
- ../marimo/docs/guides/integrating_with_marimo/custom_ui_plugins.md – Building plugin-style UI components.
- Examples: ../marimo/examples/third_party/anywidget/reactive_quak.py, ../marimo/examples/third_party/anywidget/tldraw_colorpicker.py

## API Reference – Core Utilities

[../marimo/docs/api/index.md](../marimo/docs/api/index.md)
- Summary: Top-level API map for marimo’s modules.
- Examples: None

[../marimo/docs/api/markdown.md](../marimo/docs/api/markdown.md)
- Summary: Markdown utilities, editors, and rendering helpers.
- Examples: ../marimo/examples/markdown/dynamic_markdown.py, ../marimo/examples/outputs/showing_multiple_outputs.py

[../marimo/docs/api/html.md](../marimo/docs/api/html.md)
- Summary: Reference for `mo.as_html`, `marimo.Html`, and iframe embedding helpers.
- Examples: ../marimo/examples/markdown/dynamic_markdown.py

[../marimo/docs/api/outputs.md](../marimo/docs/api/outputs.md)
- Summary: Output helpers for markdown, media, stacks, and progress widgets.
- Examples: ../marimo/examples/outputs/console_outputs.py

[../marimo/docs/api/control_flow.md](../marimo/docs/api/control_flow.md)
- Summary: Control flow utilities, gating cells, and execution helpers.
- Examples: ../marimo/examples/control_flow/stop_execution.py

[../marimo/docs/api/caching.md](../marimo/docs/api/caching.md)
- Summary: Disk and memory cache helpers to persist expensive computations.
- Examples: ../marimo/examples/running_cells/persistent_cache.py

[../marimo/docs/api/watch.md](../marimo/docs/api/watch.md)
- Summary: File watching and reactive reload helpers.
- Examples: None

[../marimo/docs/api/state.md](../marimo/docs/api/state.md)
- Summary: State container APIs including mo.state and syncing patterns.
- Examples: ../marimo/examples/misc/task_list.py

[../marimo/docs/api/inspect.md](../marimo/docs/api/inspect.md)
- Summary: Interactive inspector for exploring object attributes and documentation.
- Examples: None

[../marimo/docs/api/plotting.md](../marimo/docs/api/plotting.md)
- Summary: Chart helpers for Altair, Plotly, Matplotlib, and more.
- Examples: ../marimo/examples/outputs/plots.py

[../marimo/docs/api/diagrams.md](../marimo/docs/api/diagrams.md)
- Summary: Diagramming utilities and Mermaid integration.
- Examples: ../marimo/examples/markdown/mermaid.py

[../marimo/docs/api/query_params.md](../marimo/docs/api/query_params.md)
- Summary: Working with URL query parameters to drive notebooks.
- Examples: None

[../marimo/docs/api/cli_args.md](../marimo/docs/api/cli_args.md)
- Summary: Accessing CLI args inside notebooks.
- Examples: ../marimo/examples/running_as_a_script/with_simple_parsing.py

[../marimo/docs/api/app.md](../marimo/docs/api/app.md)
- Summary: Reference for the `marimo.App` class including run/embed helpers.
- Examples: ../marimo/docs/apps/intro.py

[../marimo/docs/api/cell.md](../marimo/docs/api/cell.md)
- Summary: Reference for the `marimo.Cell` object used to represent notebook cells.
- Examples: None

[../marimo/docs/api/status.md](../marimo/docs/api/status.md)
- Summary: Status indicator utilities for long-running tasks.
- Examples: ../marimo/examples/outputs/spinner.py

[../marimo/docs/api/miscellaneous.md](../marimo/docs/api/miscellaneous.md)
- Summary: Miscellaneous utilities and helpers not covered elsewhere.
- Examples: None

## Inputs Reference

[../marimo/docs/api/inputs/index.md](../marimo/docs/api/inputs/index.md)
- Summary: Entry point to all marimo input components.
- Examples: ../marimo/examples/ui/README.md

**Component documents:**
- ../marimo/docs/api/inputs/slider.md
- ../marimo/docs/api/inputs/range_slider.md
- ../marimo/docs/api/inputs/number.md
- ../marimo/docs/api/inputs/text.md
- ../marimo/docs/api/inputs/text_area.md
- ../marimo/docs/api/inputs/button.md
- ../marimo/docs/api/inputs/run_button.md
- ../marimo/docs/api/inputs/checkbox.md
- ../marimo/docs/api/inputs/switch.md
- ../marimo/docs/api/inputs/dropdown.md
- ../marimo/docs/api/inputs/multiselect.md
- ../marimo/docs/api/inputs/radio.md
- ../marimo/docs/api/inputs/dates.md
- ../marimo/docs/api/inputs/file.md
- ../marimo/docs/api/inputs/file_browser.md
- ../marimo/docs/api/inputs/array.md
- ../marimo/docs/api/inputs/dictionary.md
- ../marimo/docs/api/inputs/batch.md
- ../marimo/docs/api/inputs/form.md
- ../marimo/docs/api/inputs/nav_menu.md
- ../marimo/docs/api/inputs/tabs.md
- ../marimo/docs/api/inputs/chat.md
- ../marimo/docs/api/inputs/code_editor.md
- ../marimo/docs/api/inputs/data_editor.md
- ../marimo/docs/api/inputs/data_explorer.md
- ../marimo/docs/api/inputs/dataframe.md
- ../marimo/docs/api/inputs/table.md
- ../marimo/docs/api/inputs/microphone.md
- ../marimo/docs/api/inputs/refresh.md
- ../marimo/docs/api/inputs/anywidget.md

## Layouts Reference

[../marimo/docs/api/layouts/index.md](../marimo/docs/api/layouts/index.md)
- Summary: Layout primitives for structuring notebook UIs.
- Examples: ../marimo/examples/layouts/columns.py, ../marimo/examples/outputs/stacks.py

**Layout documents:**
- ../marimo/docs/api/layouts/plain.md
- ../marimo/docs/api/layouts/stacks.md
- ../marimo/docs/api/layouts/sidebar.md
- ../marimo/docs/api/layouts/routes.md
- ../marimo/docs/api/layouts/accordion.md
- ../marimo/docs/api/layouts/callout.md
- ../marimo/docs/api/layouts/json.md
- ../marimo/docs/api/layouts/tree.md
- ../marimo/docs/api/layouts/stat.md
- ../marimo/docs/api/layouts/lazy.md
- ../marimo/docs/api/layouts/carousel.md
- ../marimo/docs/api/layouts/justify.md

## Media Reference

[../marimo/docs/api/media/index.md](../marimo/docs/api/media/index.md)
- Summary: Media helpers for audio, video, PDFs, downloads, and more.
- Examples: ../marimo/examples/outputs/audio.py, ../marimo/examples/ui/download.py

**Media documents:**
- ../marimo/docs/api/media/image.md
- ../marimo/docs/api/media/image_compare.md
- ../marimo/docs/api/media/audio.md
- ../marimo/docs/api/media/video.md
- ../marimo/docs/api/media/pdf.md
- ../marimo/docs/api/media/plain_text.md
- ../marimo/docs/api/media/download.md

## Integrations Reference

[../marimo/docs/integrations/index.md](../marimo/docs/integrations/index.md)
- Summary: Overview of supported integrations and connection guides.
- Examples: ../marimo/examples/sql/connect_to_motherduck.py
- ../marimo/docs/integrations/motherduck.md – MotherDuck connection patterns.
- ../marimo/docs/integrations/google_cloud_bigquery.md – BigQuery setup and querying.
- ../marimo/docs/integrations/google_sheets.md – Google Sheets integration walkthrough.
- ../marimo/docs/integrations/google_cloud_storage.md – Working with GCS buckets.

## Documentation Apps

[../marimo/docs/apps/README.md](../marimo/docs/apps/README.md)
- Summary: Notes about documentation apps shipped with marimo.
- Examples: ../marimo/docs/apps/intro.py, ../marimo/docs/apps/output.py

**Reference apps:**
- ../marimo/docs/apps/intro.py
- ../marimo/docs/apps/output.py
- ../marimo/docs/apps/sql.py
- ../marimo/docs/apps/motherduck.py
- ../marimo/docs/apps/embedding_numbers.py
- ../marimo/docs/apps/readme_ui.py

## Embedded Example Guides

[../marimo/docs/examples/index.md](../marimo/docs/examples/index.md)
- Summary: Curated gallery landing page covering running cells, visual outputs, data workflows, and interactive input elements via card-based navigation.
- Examples: Notebook counterparts live in ../marimo/examples/ (for example running_cells/basics.py, outputs/plots.py, ui/slider.py).
- Running Cells cards:
  - async_await.md
  - basics.md
  - debugging.md
  - memory_cache.md
  - multiple_definitions.md
  - persistent_cache.md
  - refresh.md
  - run_button.md
  - stop.md
- Visual outputs & layouts:
  - basic_output.md
  - basic_markdown.md
  - capture_console_outputs.md
  - conditional_output.md
  - console_outputs.md
  - dataframes.md
  - multiple_outputs.md
  - plots.md
  - progress_bar.md
  - spinner.md
  - stacks.md
  - ../api/media/index.md
  - ../api/layouts/accordion.md
  - ../api/inputs/tabs.md
- Markdown demos:
  - admonitions.md
  - details.md
  - dynamic_markdown.md
  - emoji.md
  - mermaid.md
- Working with data call-outs:
  - ../guides/working_with_data/dataframes.md
  - ../guides/working_with_data/plotting.md
  - ../guides/working_with_data/plotting.md#plotly
  - ../guides/working_with_data/sql.md#example
  - ../guides/working_with_data/sql.md#connecting-to-a-custom-database
  - ../api/plotting.md#reactive-charts-with-altair
  - ../api/inputs/table.md
  - ../api/inputs/data_editor.md
  - ../api/inputs/dataframe.md
- Input references:
  - ../api/inputs/index.md
  - ../guides/interactivity.md
- Input elements — basic:
  - ../api/inputs/slider.md
  - ../api/inputs/dropdown.md
  - ../api/inputs/multiselect.md
  - ../api/inputs/radio.md
  - ../api/inputs/checkbox.md
  - ../api/inputs/dates.md
  - ../api/inputs/file.md
  - ../api/inputs/text.md
  - ../api/inputs/text_area.md
  - ../api/inputs/code_editor.md
  - ../api/inputs/microphone.md
  - ../api/inputs/chat.md
- Input elements — composite:
  - ../api/inputs/form.md
  - ../api/inputs/array.md
  - ../api/inputs/dictionary.md

## Example Notebooks – Directory Highlights

### Running Cells & Control Flow (../marimo/examples/running_cells/, ../marimo/examples/control_flow/)
- Highlights: basics.py, multiple_definitions.py, in_memory_cache.py, async_await.py, debugging.py, persistent_cache.py, control_flow/stop_execution.py.
- Related docs: ../marimo/docs/guides/reactivity.md, ../marimo/docs/api/control_flow.md, ../marimo/docs/api/caching.md.

### Outputs & Markdown (../marimo/examples/outputs/, ../marimo/examples/markdown/)
- Highlights: basic_output.py, showing_multiple_outputs.py, dataframes.py, plots.py, progress_bar.py, stacks.py, dynamic_markdown.py, mermaid.py, emoji.py.
- Related docs: ../marimo/docs/guides/outputs.md, ../marimo/docs/api/markdown.md, ../marimo/docs/api/media/index.md.

### Layouts (../marimo/examples/layouts/)
- Highlights: grid-dashboard.py, columns.py, sidebar.py, slides.py, plus layout metadata (layouts/grid-dashboard.grid.json, layouts/slides.slides.json).
- Related docs: ../marimo/docs/guides/apps.md, ../marimo/docs/api/layouts/index.md.

### UI Components (../marimo/examples/ui/)
- Highlights: Notebooks for sliders, text inputs, buttons, run buttons, checkboxes, radio, dropdown, multiselect, number, range slider, date/datetime, file/file_browser, tabs, forms/batch/array/dictionary, data editor, dataframe transformer, data explorer, tables, chat, code editor, microphone, refresh, switch, download, image comparison, layout stacking, plus README.md.
- Related docs: ../marimo/docs/api/inputs/index.md, ../marimo/docs/api/media/index.md.

### SQL & Data (../marimo/examples/sql/)
- Highlights: README.md, querying_dataframes.py, connect_to_postgres.py, connect_to_motherduck.py, parameterized queries, CSV/JSON/Parquet readers, dashboards under misc/.
- Related docs: ../marimo/docs/guides/working_with_data/sql.md, ../marimo/docs/integrations/index.md.

### AI Workflows (../marimo/examples/ai/)
- Highlights: Chat integrations (OpenAI, Anthropic, Gemini, Groq, DeepSeek, Bedrock, MLX), tool-enabled notebooks (tools/*.py), dataset labeling/model comparison (data/*.py), and miscellaneous AI demos (misc/*.py).
- Related docs: ../marimo/docs/guides/generate_with_ai/index.md, ../marimo/docs/guides/editor_features/ai_completion.md.

### Cloud & Deployment (../marimo/examples/cloud/)
- Highlights: README.md, GCP integrations (gcp/*.py), Modal deployment (modal/*.py with modal_app.py, modal_edit.py, nbs/notebook.py).
- Related docs: ../marimo/docs/guides/deploying/index.md, ../marimo/docs/integrations/google_cloud_storage.md.

### Framework Integrations (../marimo/examples/frameworks/)
- Highlights: FastAPI, Flask, FastAPI + GitHub OAuth, Fasthtml demos, templates, and README files.
- Related docs: ../marimo/docs/guides/deploying/programmatically.md, ../marimo/docs/guides/deploying/authentication.md.

### Third-Party Ecosystem (../marimo/examples/third_party/)
- Highlights: Subdirectories for AnyWidget, A-Frame, Chroma, CVXPY, Databricks, DuckDB, Great Tables, Hugging Face, Ibis, Leafmap, Matplotlib, MotherDuck, NVIDIA, Plotly, Polars, Pygwalker, PyIceberg, Pymde, Sage, Substrate, Unsloth—each with README (where provided) and demo notebooks.
- Related docs: ../marimo/docs/integrations/index.md, ../marimo/docs/guides/integrating_with_marimo/custom_ui_plugins.md.

### Testing (../marimo/examples/testing/)
- Highlights: README.md, test_with_pytest.py, running_doctests.py.
- Related docs: ../marimo/docs/guides/testing/index.md.

### Miscellaneous Demos (../marimo/examples/misc/)
- Highlights: Public folders, task lists, filterable tables, seam carving, Bayes theorem, compound interest, mortgage calculators, ISS tracker, Pokémon stats, reactive plots, monotonic splines, colliding blocks vs π, custom configuration, create-your-own shape, movies-by-decade, explore-your-own-data, notebook directory handling.
- Related docs: ../marimo/docs/guides/state.md, ../marimo/docs/guides/outputs.md, ../marimo/docs/guides/package_management/index.md.

### Running as a Script (../marimo/examples/running_as_a_script/)
- Highlights: with_argparse.py, with_simple_parsing.py, sharing_arguments.py, textual_app.py.
- Related docs: ../marimo/docs/guides/scripts.md, ../marimo/docs/api/cli_args.md.

### Cloud Modal Assets (../marimo/examples/cloud/modal/)
- Highlights: modal_app.py, modal_edit.py, README.md, notebooks under nbs/notebook.py.
- Related docs: ../marimo/docs/guides/deploying/index.md, ../marimo/docs/guides/deploying/prebuilt_containers.md.

## README Files & Additional Notes
- ../marimo/examples/README.md
- ../marimo/examples/cloud/README.md
- ../marimo/examples/ui/README.md
- ../marimo/examples/sql/README.md
- ../marimo/examples/testing/README.md
- ../marimo/examples/misc/README.md
- ../marimo/examples/third_party/README.md

## Supporting Content

[../marimo/docs/_static/CLAUDE.md](../marimo/docs/_static/CLAUDE.md)
- Summary: AI assistant instructions embedded in the documentation static assets.
- Examples: None

[../marimo/docs/stylesheets/extra.css](../marimo/docs/stylesheets/extra.css)
- Summary: Custom stylesheet referenced by theming guides.
- Examples: None

[../marimo/docs/blocks.py](../marimo/docs/blocks.py)
- Summary: MkDocs-specific block definitions used during site generation.
- Examples: None

[../marimo/docs/hooks.py](../marimo/docs/hooks.py)
- Summary: MkDocs hook that scans rendered pages for missing /_static asset references and logs warnings during builds.
- Examples: None

## Example Notebooks – Full Listings

### AI Workflows (../marimo/examples/ai/)
- README.md
- chat/README.md, chat/anthropic_example.py, chat/bedrock_example.py, chat/custom.py, chat/dagger_code_interpreter.py, chat/deepseek_example.py, chat/gemini.py, chat/generative_ui.py, chat/groq_example.py, chat/llm_datasette.py, chat/mlx_chat.py, chat/openai_example.py, chat/recipe_bot.py, chat/simplemind_example.py
- data/data_labeler.py, data/model_comparison.py
- misc/build_a_superhero.py, misc/micrograd_mlp.py, misc/pdf_question_answer.py
- tools/README.md, tools/chat_with_tools.py, tools/code_interpreter.py, tools/dataset_analysis.py

### Cloud & Deployment (../marimo/examples/cloud/)
- README.md
- gcp/google_cloud_bigquery.py, gcp/google_cloud_storage.py, gcp/google_sheets.py
- modal/README.md, modal/modal_app.py, modal/modal_edit.py, modal/nbs/notebook.py

### Control Flow (../marimo/examples/control_flow/)
- README.md, stop_execution.py

### Framework Integrations (../marimo/examples/frameworks/)
- README.md
- fastapi/README.md, fastapi/main.py, fastapi/templates/home.html, fastapi/templates/login.html
- fastapi-endpoint/README.md, fastapi-endpoint/main.py, fastapi-endpoint/notebook.py
- fastapi-github/README.md, fastapi-github/main.py, fastapi-github/templates/home.html
- fasthtml/.gitignore, fasthtml/README.md, fasthtml/main.py
- flask/.gitignore, flask/README.md, flask/main.py, flask/templates/error.html, flask/templates/home.html, flask/templates/login.html

### Layouts (../marimo/examples/layouts/)
- README.md, columns.py, grid-dashboard.py, sidebar.py, slides.py
- layouts/grid-dashboard.grid.json, layouts/slides.slides.json

### Markdown (../marimo/examples/markdown/)
- README.md, admonitions.py, details.py, dynamic_markdown.py, emoji.py, mermaid.py

### Miscellaneous (../marimo/examples/misc/)
- README.md, bayes_theorem.py, colliding_blocks_and_pi.py, compound_interest.py, create_your_own_shape.py, custom_configuration.py, explore_your_own_data.py, filterable_table.py, iss.py, monotonic_splines.py, mortgage_calculator.py, movies_by_the_decade.py, notebook_dir.py, pokemon_stats.py, public/marimos.webp, public_folder.py, reactive_plots.py, seam_carving.py, task_list.py

### Output Patterns (../marimo/examples/outputs/)
- accordion.py, audio.py, basic_markdown.py, capture_console_outputs.py, cell_output.py, conditional_output.py, console_outputs.py, dataframes.py, plots.py, progress_bar.py, showing_multiple_outputs.py, spinner.py, stacks.py

### Running as a Script (../marimo/examples/running_as_a_script/)
- sharing_arguments.py, textual_app.py, with_argparse.py, with_simple_parsing.py

### Running Cells (../marimo/examples/running_cells/)
- async_await.py, basics.py, debugging.py, in_memory_cache.py, multiple_definitions.py, persistent_cache.py

### SQL & Data (../marimo/examples/sql/)
- README.md, connect_to_motherduck.py, connect_to_persistent_db.py, connect_to_postgres.py, connect_to_sqlite.py, duckdb_example.py, histograms.py, misc/README.md, misc/database_explorer.py, misc/electric_vehicles.py, misc/sql_cars.py, parametrizing_sql_queries.py, querying_dataframes.py, read_csv.py, read_json.py, read_parquet.py

### Testing (../marimo/examples/testing/)
- README.md, running_doctests.py, test_with_pytest.py

### Third-Party Ecosystem (../marimo/examples/third_party/)
- README.md
- aframe/aframe_example.py
- anywidget/reactive_quak.py, anywidget/tldraw_colorpicker.py
- chroma/multimodal_retrieval.py
- cvxpy/regularization_and_sparsity.py, cvxpy/signals/app.py, cvxpy/signals/examples.py, cvxpy/signals/modules/__init__.py, cvxpy/signals/modules/components.py, cvxpy/signals/modules/dataloaders.py, cvxpy/signals/modules/explainer.py, cvxpy/signals/modules/intro_problem.py, cvxpy/signals/modules/layout.py, cvxpy/signals/modules/problems.py, cvxpy/signals/modules/solutions.py, cvxpy/signals/assets/solar_power_soiling_reference.png, cvxpy/smallest_enclosing_circle.py
- databricks/databricks_connect.py
- duckdb/duckdb_example.py
- great_tables/coffee-sales.json, great_tables/great_tables_example.py
- huggingface/README.md, huggingface/chatbot.py, huggingface/text-to-image.py
- ibis/ibis_example.py
- leafmap/leafmap_example.py
- matplotlib/mandelbrot.py, matplotlib/surfaces.py
- motherduck/embeddings/README.md, motherduck/embeddings/embeddings_explorer.py, motherduck/embeddings/embeddings_explorer_final.py
- nvidia/nims.py
- plotly/image_selection.py, plotly/mapbox.py, plotly/scatter_map.py
- polars/polars_example.py
- pygwalker/example.py
- pyiceberg/data_catalog.py
- pymde/complete_graph.py, pymde/debugging_embeddings.py, pymde/drawing_graphs.py, pymde/embedding_numbers.py, pymde/google_scholar.py, pymde/interactive_cluster_analysis.py, pymde/rotational_invariance.py, pymde/tree.py, pymde/us_counties.py
- sage/README.md, sage/chat_with_github_repo.py, sage/chat_with_sage.png, sage/continue_chatting_with_sage.png
- substrate/video_generation.py
- unsloth/llama_3_1_8b_2x_faster_finetuning.py, unsloth/requirements.txt
