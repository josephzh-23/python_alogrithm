package Basics

import java.awt.Point
var MAP_SIZE_COL = 10
var MAP_SIZE_ROW= 21
private val mPoints: Array<Array<Point>> = Array(MAP_SIZE_ROW) {
    Array(MAP_SIZE_COL) { Point(0, 0) }
}