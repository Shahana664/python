class Messenger:
    
    def send_messege(self):
        print("iam sending messege")
        def recieve_messege(self):
            print("iam recieving messege")
            
            
            
            class FMessenge(Messenger):
                def send_messege(self):
                    print("iam sending messege using Facebook")
                    def recieve_messege(self):
                        print("iam recieving messege using a Facebook")
                        
                        
                        class WMessenge(Messenger):
                            def send_messege(self):
                                print("iam sending messege using Whatsup")
                                def recieve_messege(self):
                                    print("iam recieving messege using Whatsup")
                                    
                                    
                                    class Instagram(Messenger):
                                        def send_messege(self):
                                            print("iam sending messege using Instagram")
                                            def recieve_messege(self):
                                                print("iam recieving messege using Instagram")
                                                
                                                
                                                def display(ref):
                                                    ref.send_messege()
                                                    ref.recieve_messege()
                                                    
                                                    
                                                    F=FacebookMessenger
                                                    W=WhatsupMessenger
                                                    I=InstagramMessenger
                                                    
                                                    f.display(F)
                                                    f.display(W)
                                                    f.display(I)
            