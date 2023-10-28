import javax.swing.*;
import java.awt.*;

public class MyFrame extends JFrame{
    JLabel headingLabel;
    JPanel headingPanel;
    MyFrame(){
        //========================Heading========================//
        headingLabel = new JLabel(" \uD83D\uDC9D    Heart Disease Predictor");  //https://www.alt-codes.net/heart_alt_code.php
        headingLabel.setForeground(new Color(222, 174, 9));
        headingLabel.setBounds(0,0,700,55);
        headingLabel.setFont(new Font("Monospaced" , Font.BOLD , 35));

        headingPanel = new JPanel();
        headingPanel.setBounds(0,0,750,60);
        headingPanel.setBackground(new Color(30, 1, 51));
        headingPanel.add(headingLabel);
        headingPanel.setLayout(null);
        //========================Heading========================//


        this.setTitle("Heart Disease Predictor");
        this.getContentPane().setBackground(new Color(3, 4, 40));
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.setSize(750 , 750);
        this.setVisible(true);
        this.setLayout(null);
        this.add(headingPanel);
    }
}
