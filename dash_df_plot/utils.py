import pandas as pd

# from fpbiolib.df_storage import redis_store

from .ids import ids
from importlib.metadata import version

__version__ = version("dash_df_plot")


# def reset_df_stores(session_id=""):
#     """On page reload, reset df stores with empty
#     dataframes, and filenames.
#     """
#     df = pd.DataFrame()
#     redis_store.pickle_save(df, key=session_id + ids.trace_df_store.id())
#     redis_store.pickle_save(df, key=session_id + ids.sel_trace_df_store.id())
#     redis_store.pickle_save(df, key=session_id + ids.main_graph_trace_df_store.id())
#     redis_store.pickle_save(df, key=session_id + ids.cow_trace_df_store.id())
#     redis_store.pickle_save(df, key=session_id + ids.ftir_subtr_trace_df_store.id())
#     redis_store.pickle_save(df, key=session_id + ids.label_df_store.id())
#     redis_store.pickle_save(df, key=session_id + ids.control_parameters_table_df.id())
#     redis_store.pickle_save(["Uploaded: "], key=session_id + ids.filename_store.id())
#     redis_store.pickle_save(df, key=session_id + ids.trace_similarity_table_df.id())
