Philip has written a Python function `all_pairs_shortest_paths(adj_list)` that calculates the length of the shortest paths between all node pairs in an undirected graph.  Your task is to help Philip test the correctness of `all_pairs_shortest_paths` function.

For an undirected graph G with N nodes, `adj_list` is a list with E elements where each element is a triple (3-tuple) in which the first and second elements are names of nodes (strings) and the third element is the weight of an edge between these nodes (integer).  The function raises ValueError exception if the graph is not connected or any of the weights is zero or negative or there are multiple edges between any pair of nodes or there are loops (i.e., an edge from a node to itself).  The function returns a list of (N * (N-1) / 2) triples in which the first and second elements are names of nodes (strings) and the third element is the length of the shortest path between these nodes (integer).

Submit your tests in a single file named *test_impl.py*.

You should assume the UUT is available in _impl.py_ file.  So, in your test file, you should use appropriate import statement and name qualification to access the implementation.  Composability of your tests with our implementation is worth 1 point.

To evaluate your tests, we will use PyTest.  We will execute the command pytest-2.9.x in a folder with your *test_impl.py* file and our _impl.py_ files, i.e., one execution of pytest-2.9.x for each variant of our implementation.

Please resolve any ambiguities about the problem by discussing them with the users (TA or instructor) via email or in-person.  When you identify ambiguities, try to describe them precisely and pose questions about them that will help remove ambiguities.

P.S.: If your tests can check correctness of the function without recalculating the lengths of all pairs shortest paths or doing something equally complex, then you deserve few extra credit points :)  If you want us to consider your submission for extra credits, then please leave a comment "consider for extra credit" with your submission and explain how your tests accomplish this feat within comments at the end of your submission file.  This applies to non-example based tests only.
