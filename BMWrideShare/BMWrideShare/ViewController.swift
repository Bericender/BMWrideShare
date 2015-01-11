//
//  ViewController.swift
//  BMWrideShare
//
//  Created by psxge on 10/01/15.
//  Copyright (c) 2015 Htd. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBAction func onStart(sender: AnyObject) {
        self.performSegueWithIdentifier("fromStartToMainSegue", sender: self)
        
    }
    @IBOutlet weak var FrontRightSeat: UIImageView!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func toggleFrontRight() {
        if (self.FrontRightSeat.alpha == 0) {
            self.FrontRightSeat.alpha = 1
        } else {
            self.FrontRightSeat.alpha = 0
        }
    }


    @IBAction func onButton(sender: AnyObject) {
        toggleFrontRight()
    }
}

