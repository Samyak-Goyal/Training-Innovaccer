import { render,screen } from "@testing-library/react"
import Async from "./Async"

describe('Async Component',()=>{
    // test('if posts is fetched', async()=>{
    //     render(<Async/>);
    //     const listElement= await screen.findAllByRole(`list`);
    //     expect(listElement).not.toHaveLength(0);
    // })
    test('mock test fetch', async()=>{
        window.fetch = jest.fn();
        window.fetch.mockResolvedValueOnce({
            json: async () => [{id:"p1", title:"Post 1"}],
        });

        render(<Async/>);
        const listElement= await screen.findAllByRole(`list`);
        expect(listElement).not.toHaveLength(0);
    })
})