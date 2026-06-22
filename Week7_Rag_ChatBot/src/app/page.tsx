import Image from "next/image";

export default function Home() {
  return (
    <div className="font-sans grid grid-rows-[20px_1fr_20px] items-center justify-items-center h-full p-8 pb-10 gap-12 sm:p-20 mt-0 pt-0">
      <main className="flex flex-col gap-[28px] row-start-2 items-center sm:items-start bg-blue-100 py-8 px-18 rounded-xl">
        <div className="text-7xl font-bold">RAG BOT</div>
        <ol className="font-mono list-inside list-decimal text-sm/6 text-center sm:text-left">
          <li className="mb-2 tracking-[-.01em]">
            Get started by uploading document.
          </li>
          <li className="tracking-[-.01em] mb-2">
            Ask the bot your questions form the same.
          </li>
          <li className="tracking-[-.01em]">
            Enjoy the concise answers!
          </li>
        </ol>

        <div className="flex gap-4 items-center flex-col sm:flex-row">
          <a
            className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:w-auto"
            href="/upload"
            rel="noopener noreferrer"
          >
            <Image
              className="dark:invert"
              src="/vercel.svg"
              alt="Vercel logomark"
              width={20}
              height={20}
            />
            Upload Document
          </a>
          <a
            className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 w-full sm:w-auto md:w-[158px]"
            href="/chat"
            rel="noopener noreferrer"
          >
            Go To ChatBot
          </a>
        </div>
      </main>
    </div>
  );
}
