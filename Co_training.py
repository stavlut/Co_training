

class Co_training:
    def __init__(self,labeled_data,unlabed_data,view1,view2,base_learner,number_of_iterations,unlabeled_records_added):
        self.labeled_data = labeled_data;
        self.unlabed_data = unlabed_data;
        self.view1 = view1;
        self.view2 = view2;
        self.base_learner1 = base_learner;
        self.base_learner2 = base_learner;
        self.number_of_iterations = number_of_iterations;
        self.unlabeled_records_added = unlabeled_records_added;

    def fit(self):
        return

    def predict(self):
        return

    def project(self,labeled_data,unlabed_data,view1,view2):

        # return L1,L2,U1,U2
        return

    def select_top_n(self,unlabeled_records_added):

        return

    