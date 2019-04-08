# -------------------- PATH ---------------------

#ROOT_PATH = "/local/data2/pxu4/TypeClassification"
ROOT_PATH = "."
DATA_PATH = "%s/data" % ROOT_PATH
WIKI_DATA_PATH = "%s/corpus/Wiki" % DATA_PATH
ONTONOTES_DATA_PATH = "%s/corpus/OntoNotes" % DATA_PATH
WIKIM_DATA_PATH = "%s/wiki_modified" % DATA_PATH
BBN_DATA_PATH = "%s/BBN" % DATA_PATH

LOG_DIR = "%s/log" % ROOT_PATH
CHECKPOINT_DIR = "%s/checkpoint" % ROOT_PATH
OUTPUT_DIR = "%s/output" % ROOT_PATH

# -------------------- DATA ----------------------

WIKI_ALL = "%s/all.json" % WIKI_DATA_PATH
WIKI_TRAIN = "%s/train.json" % WIKI_DATA_PATH
WIKI_VALID = "%s/dev.json" % WIKI_DATA_PATH
WIKI_TEST = "%s/test.json" % WIKI_DATA_PATH

WIKI_TYPE = "%s/type.pkl" % WIKI_DATA_PATH
WIKI_TRAIN_CLEAN = "%s/train_clean.tsv" % WIKI_DATA_PATH
WIKI_TEST_CLEAN = "%s/test_clean.tsv" % WIKI_DATA_PATH

ONTONOTES_ALL = "%s/all.json" % ONTONOTES_DATA_PATH
ONTONOTES_TRAIN = "%s/train.json" % ONTONOTES_DATA_PATH
ONTONOTES_VALID = "%s/dev.json" % ONTONOTES_DATA_PATH
ONTONOTES_TEST = "%s/test.json" % ONTONOTES_DATA_PATH

ONTONOTES_TYPE = "%s/type.pkl" % ONTONOTES_DATA_PATH
ONTONOTES_TRAIN_CLEAN = "%s/train_clean.tsv" % ONTONOTES_DATA_PATH
ONTONOTES_TEST_CLEAN = "%s/test_clean.tsv" % ONTONOTES_DATA_PATH

BBN_ALL = "%s/all.json" % BBN_DATA_PATH
BBN_TRAIN = "%s/train.json" % BBN_DATA_PATH
BBN_VALID = "%s/dev.json" % BBN_DATA_PATH
BBN_TEST = "%s/test.json" % BBN_DATA_PATH

BBN_TYPE = "%s/type.pkl" % BBN_DATA_PATH
BBN_TRAIN_CLEAN = "%s/train_clean.tsv" % BBN_DATA_PATH
BBN_TEST_CLEAN = "%s/test_clean.tsv" % BBN_DATA_PATH

WIKIM_ALL = "%s/all.json" % WIKIM_DATA_PATH
WIKIM_TRAIN = "%s/train.json" % WIKIM_DATA_PATH
WIKIM_VALID = "%s/dev.json" % WIKIM_DATA_PATH
WIKIM_TEST = "%s/test.json" % WIKIM_DATA_PATH

WIKIM_TYPE = "%s/type.pkl" % WIKIM_DATA_PATH
WIKIM_TRAIN_CLEAN = "%s/train_clean.tsv" % WIKIM_DATA_PATH
WIKIM_TEST_CLEAN = "%s/test_clean.tsv" % WIKIM_DATA_PATH

WIKI_MAPPING = "%s/wiki_mapping.txt" % DATA_PATH

EMBEDDING_DATA = "%s/glove.840B.300d.txt" % DATA_PATH

# --------------------- PARAM -----------------------

MAX_DOCUMENT_LENGTH = 30

MENTION_SIZE = 15

WINDOW_SIZE = 10

RANDOM_SEED = 2017
