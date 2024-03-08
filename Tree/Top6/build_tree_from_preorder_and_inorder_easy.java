//package Tree.Top6;
//
//import javax.swing.tree.Tree.Basic.TreeNode;
//
//class Solution3{
//
//    public Tree.Basic.TreeNode buildTree(int[] preorder, int[] inorder){
//        return helper(0, 0, inorder.length-1, preorder, inorder);
//    }
//    public Tree.Basic.TreeNode helper(int preStart, int inStart, int inEnd,
//                           int[] preorder, int[] inorder){
//
//        if(preStart > preorder.length -1 || inStart > inEnd) return null;
//
//        Tree.Basic.TreeNode root = new Tree.Basic.TreeNode(preorder[preStart]);
//
//        int inIndex = 0;
//        // Used to find the inorder root index from the preorder [] as explained
//
//        for (int i = inStart; i <= inEnd; i++){
//            if(root.value == inorder[i]){
//                inIndex = i;
//            }
//        }
//
//        root.left = helper(preStart + 1, inStart, inIndex -1,
//                preorder, inorder);
//        root.right = helper(preStart + inIndex - inStart + 1, inIndex +1,
//                inEnd, preorder, inorder);
//        return root;
//    }
//}