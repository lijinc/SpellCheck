__author__ = 'LIJIN'
import utils
class Node:
    def __init__(self,data):
        self.data=data
        self.noChildren=0
        self.children=None
class BKTree:
    def __init__(self):
        self.root=None

    def insert(self,text):
       self.root=self._insert(self.root,text)

    def _insert(self,root,text):
        if root is None:
            return Node(text)
        elif root.noChildren == 0:
            root.noChildren += 1
            dist=utils.editDistance(root.data,text)
            root.children={dist:Node(text)}
            return root
        else:
            dist = utils.editDistance(root.data,text)
            if root.children.has_key(dist):
                root.children[dist]=self._insert(root.children.get(dist),text)
            else:
                root.noChildren += 1
                root.children.update({dist:Node(text)})
            return root
    def __str__(self):
        return self._print(self.root)
    def _print(self,root):
        if root is None:
            return ""
        elif root.noChildren==0:
            return root.data+"-0"+"\n"
        else:
            string=root.data+"-"+str(root.noChildren)+"\n"
            for key in sorted(root.children.iterkeys()):
                string=string+self._print(root.children[key])
            return string
    def findClosestMatches(self,threshold,text):
        self._findClosestMatches(self.root,threshold,text)
    def _findClosestMatches(self,root,threshold,text):
        if root is None:
            return
        else:
            dist=utils.editDistance(root.data,text)
            if dist<=2:
                print(root.data)
            if root.noChildren==0:
                return
            else:
                for key in sorted(root.children.iterkeys()):
                    if key in range(dist-threshold,dist+threshold):
                        self._findClosestMatches(root.children[key],threshold,text)
