public class Eagle extends Bird {
    public Eagle(FlyBehavior flyBehavior, SwimBehavior swimBehavior) {
        super(flyBehavior, swimBehavior);
    }

    public void display() {
        System.out.println("老鹰");
        super.display();
    }
}
