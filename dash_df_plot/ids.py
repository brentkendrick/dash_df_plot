from enum import Enum, auto

app_id = "dash_df_plot"  # ensures no id conflicts on the server


class ids(Enum):
    """Provide unique component ID names to Dash components.
    Based on: https://medium.com/@draymo/some-tips-for-robust-dash-callbacks-4f97bcc4d471
    """  # noqa

    # Page container
    grid_container = auto()

    # Normalize traces
    area_normalize_switch = auto()
    peak_max_normalize_switch = auto()

    initial_x_min_id = auto()
    initial_x_max_id = auto()
    truncate_slider_id = auto()
    trace_selector_and_styling_div = auto()

    # Uploader IDs
    x_many_y_uploader = auto()
    many_x_y_uploader = auto()
    du800_csv_uploader = auto()
    du800_dux_uploader = auto()
    nanodrop_tsv_uploader = auto()
    solovpe_csv_uploader = auto()
    filereader_parser_uploader = auto()
    shrink_trace_data = auto()
    peak_label_uploader = auto()

    import_status = auto()
    uploader_modal = auto()
    add_file_button = auto()
    trace_refresh_webpage_btn = auto()

    # Dataframes
    trace_df_store = auto()
    sel_trace_df_store = auto()
    main_graph_trace_df_store = auto()
    cow_trace_df_store = auto()
    ftir_subtr_trace_df_store = auto()
    label_df_store = auto()

    # Dataframe columns
    trace_df_col_store = auto()

    # Filenames
    current_uploaded_filename_store = auto()
    filename_store = auto()

    # Main graph component IDs
    main_graph = auto()

    # Trace selection, coloring, line formatting and naming
    selected_traces = auto()
    selected_traces_store = auto()
    selected_traces_idx = auto()
    selected_traces_idx_store = auto()

    rename_traces_store = auto()

    trace_color_picker = auto()
    trace_line_width = auto()
    trace_line_type = auto()
    trace_selector = auto()

    trace_color_picker_modal = auto()
    selected_trace_dash = auto()
    selected_trace_width = auto()
    selected_trace_line_formatting_idx = auto()
    trace_color = auto()
    selected_trace_colors = auto()

    reference_trace_dropdown = auto()
    reference_trace_store = auto()
    subtract_trace_dropdown = auto()
    subtract_trace_store = auto()

    graph_formatting_modal = auto()
    graph_formatting_modal_btn = auto()

    rename_trace_input = auto()
    selected_trace_indices = auto()
    cdf_graph = auto()
    cdf_download = auto()

    trace_selection_alert_div = auto()
    trace_selection_naming_coloring_collapse = auto()
    trace_selection_naming_coloring_btn = auto()

    # Outputs
    control_parameters_table = auto()
    control_parameters_table_df = auto()
    main_graph_control_parameters = auto()
    trace_similarity_table = auto()
    trace_similarity_table_df = auto()
    legend_position = auto()
    hide_reference_trace = auto()

    def id(self, index=None):
        if index is None:
            return f"{self.name}-{app_id}"
        return f"{self.name}-{app_id}"
