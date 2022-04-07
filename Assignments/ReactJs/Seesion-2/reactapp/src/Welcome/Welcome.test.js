import {render, screen} from "@testing-library/react"
import Welcome from "./Welcome"
import userEvent from "@testing-library/user-event"
describe("Welcome",()=>{
    test("renders hello world",()=>{
        render(<Welcome/>);
        const hello_world= screen.getByText("Hello world",{exact: false});
        expect(hello_world).toBeInTheDocument();
    });
    test("renders good morning",()=>{
        render(<Welcome/>);
        const hello_world= screen.getByText("Hello world",{exact: false});
        expect(hello_world).toBeInTheDocument();
    });
    test("renders if button not clicked",()=>{
        render(<Welcome/>);
        const notclicked= screen.getByText("morning",{exact: false});
        expect(notclicked).toBeInTheDocument();
    });
    test("renders if button clicked",()=>{
        render(<Welcome/>);
        const buttonElement=screen.getByRole("button")
        userEvent.click(buttonElement)
        const clicked= screen.getByText("night",{exact: false});
        expect(clicked).toBeInTheDocument();
    });
    test("removes good morning when button is clicked",()=>{
        render(<Welcome/>);
        const buttonElement=screen.getByRole("button")
        userEvent.click(buttonElement)
        const clicked= screen.queryByText("morning",{exact: false});
        expect(clicked).toBeNull();
    });
})


