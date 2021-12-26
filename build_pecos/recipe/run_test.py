from scipy.sparse import load_npz
from pecos.xmc.xlinear.model import XLinearModel
from pecos.xmc import Indexer, LabelEmbeddingFactory


def main():
    X = load_npz('test/tst-data/xmc/xlinear/X.npz')
    Y = load_npz('test/tst-data/xmc/xlinear/Y.npz')

    label_feat = LabelEmbeddingFactory.create(Y, X)
    cluster_chain = Indexer.gen(label_feat)
    model = XLinearModel.train(X, Y, C=cluster_chain)
    model.save("./save-models")


if __name__ == "__main__":
    main()
