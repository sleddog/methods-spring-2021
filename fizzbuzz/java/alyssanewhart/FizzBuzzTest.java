import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class FizzBuzzTest {
    
    @Test
    public void testFizz() {
        Assertions.assertEquals("Fizz", FizzBuzz.FizzBuzz(3));
    }
    
    @Test
    public void testBuzz() {
        Assertions.assertEquals("Buzz", FizzBuzz.FizzBuzz(5));
    }
    
    @Test
    public void testPing() {
        Assertions.assertEquals("Ping", FizzBuzz.FizzBuzz(7));
    }
    
    @Test
    public void testPong() {
        Assertions.assertEquals("Pong", FizzBuzz.FizzBuzz(11));
    }
    
    @Test
    public void testFizzBuzz() {
        Assertions.assertEquals("FizzBuzz", FizzBuzz.FizzBuzz(15));
    }
    
    @Test
    public void testFizzPing() {
        Assertions.assertEquals("FizzPing", FizzBuzz.FizzBuzz(21));
    }
    
    @Test
    public void testFizzPong() {
        Assertions.assertEquals("FizzPong", FizzBuzz.FizzBuzz(33));
    }
    
    @Test
    public void testBuzzPing() {
        Assertions.assertEquals("BuzzPing", FizzBuzz.FizzBuzz(35));
    }
    
    @Test
    public void testBuzzPong() {
        Assertions.assertEquals("BuzzPong", FizzBuzz.FizzBuzz(55));
    }
    
    @Test
    public void testPingPong() {
        Assertions.assertEquals("PingPong", FizzBuzz.FizzBuzz(77));
    }
    
    @Test
    public void testFizzBuzzPing() {
        Assertions.assertEquals("FizzBuzzPing", FizzBuzz.FizzBuzz(105));
    }
    
    @Test
    public void testFizzBuzzPong() {
        Assertions.assertEquals("FizzBuzzPong", FizzBuzz.FizzBuzz(165));
    }

    @Test
    public void testFizzPingPong() {
        Assertions.assertEquals("FizzPingPong", FizzBuzz.FizzBuzz(231));
    }
    
    @Test
    public void testBuzzPingPong() {
        Assertions.assertEquals("BuzzPingPong", FizzBuzz.FizzBuzz(385));
    }
    
    @Test
    public void testFizzBuzzPingPong() {
        Assertions.assertEquals("FizzBuzzPingPong", FizzBuzz.FizzBuzz(1155));
    }
}
