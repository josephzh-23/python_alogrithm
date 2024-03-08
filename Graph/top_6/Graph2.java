//package Graph.Top_6;
//
//
//import java.util.ArrayList;
//import java.util.HashMap;
//
//
//class Graph2 {
//
//
//	private ArrayList<Project2> nodes = new ArrayList<Project2>();
//	private HashMap<String, Project2> map = new HashMap<String, Project2>();
//
//	public Project2 getOrCreateNode(String name) {
//		if(!map.containsKey(name)) {
//			Project2 node = new Project2(name);
//			nodes.add(node);
//			map.put(name, node);
//		}
//		return map.get(name);
//	}
//
//	public void addEdge(String startName, String endName) {
//		Project2 start = getOrCreateNode(startName);
//		Project2 end = getOrCreateNode(endName);
//		start.addNeighbor(end);
//	}
//
//	public ArrayList<Project2> getNodes() {	return nodes;	}
//
//
//	static Graph2 buildGraph(String[] projects, String[][] dependencies) {
//		Graph2 graph2 = new Graph2();
//		for (String project : projects)
//			graph2.getOrCreateNode(project);
//		for (String[] dependency : dependencies)
//			graph2.addEdge(dependency[0], dependency[1]);
//		return graph2;
//	}
//
//	Project2[] orderProjects(ArrayList<Project2> projects) {
//		Project2[] order = new Project2[projects.size()];
//		int endOfList = addNonDependent(order, projects, 0);
//		int toBeProcessed = 0;
//		while(toBeProcessed < order.length) {
//			Project2 current = order[toBeProcessed];
//
//			if (current == null)	return null;		// circular dependency, no remaining projects w/ 0 dependencies
//
//			ArrayList<Project2> children = current.getChildren();		// remove myself as dependency
//			for (Project2 child : children)
//				child.decrementDependencies();
//
//			endOfList = addNonDependent(order, children, endOfList);	// add children that have no one depending on them
//			++toBeProcessed;
//		}
//		return order;
//	}
//
//	/* insert projects w/ 0 dependencies into the order array */
//	static int addNonDependent(Project2[] order, ArrayList<Project2> projects, int offset) {
//		for(Project2 project : projects)
//			if (project.getNumberDependencies() == 0)
//				order[offset] = project; ++offset;
//		return offset;
//	}
//}
//
//class Project2 {
//	private ArrayList<Project2> children = new ArrayList<Project2>();
//	private HashMap<String, Project2> map = new HashMap<String, Project2>();
//	private String name;
//	private int dependencies = 0;
//
//	public Project2(String n) {	name = n;	}
//	public void addNeighbor(Project2 node) {
//		if(!map.containsKey(node.getName())) {
//			children.add(node);
//			node.incrementDependencies();
//		}
//	}
//
//	public void incrementDependencies() {	++dependencies;	 }
//	public void decrementDependencies() {	--dependencies;	 }
//	public String getName() {	return name;	}
//	public ArrayList<Project2> getChildren() {	return children;	}
//	public int getNumberDependencies() {	return dependencies;	}
//
//	public static void Sliding_window.maining_window.Sliding_window.Graph.Hard.main(String[] args) {
////		String[] arr0=new String[]{"Apple","Banana","Orange"};
////		findBuildOrder()
//
//	}
//	static Project2[] findBuildOrder(String[] projects, String[][] dependencies) {
//		Graph2 graph2 = Graph2.buildGraph(projects, dependencies);
//		return Graph2.orderProjects(graph2.getNodes());
//	}
//
//}
//
