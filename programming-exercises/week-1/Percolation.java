/**
    * Percolation description goes here
    * @author Jeury Mejia
    * @version 1.0
    * @since 08/18/2018
*/

import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

    /**
    * Creates n-by-n grid will all sites blocked
    * @param n the integer representing the number of rows and cols in grid
    * @throws java.lang.IllegalArgumentException if n <= 0
    */
    public Percolation(int n) {

    }

    /**
    * Open site(row, col) if it is not open already
    * @param row the row index of the site
    * @param col the column index of the site
    * @throws java.lang.IllegalArgumentException if any param is outside of [1,n]
    */
    public void open(int row, int col) {

    }

    /**
    * Is site (row, col) open?
    */
    public boolean isOpen(int row, int col) {

    }

    /**
    * Is site(row, col) full? A full site is an open site that can
    * be connected to an open site in the top row via a chain of
    * neighboring (left, right, up, down) open sites
    */
    public boolean isFull(int row, int col) {

    }

    /**
    * Number of open sites
    */
    public int numberOfOpenSites() {

    }

    /**
    * Does the system percolates? we say the system percolates if there is a
    * full site in the bottom row. In other words, the system percolates if we
    * fill all open sites connected in the to row and that process fills some
    * open site in bottom row
    */
    public boolean percolates() {

    }

    /**
    * Test client
    */
    public static void main(String[] args) {

    }
}
