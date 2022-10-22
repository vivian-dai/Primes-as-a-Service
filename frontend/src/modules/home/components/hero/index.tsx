import UnderlineLink from "@modules/common/components/underline-link"
import Image from "next/image"

const Hero = () => {
  return (
    <div className="h-[90vh] w-full relative" id="container">
      <svg
        className="background-navy"
        width="1759"
        height="1024"
        viewBox="0 0 1759 1024"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <rect opacity="0.9" width="1107.59" height="1024" fill="#181168" />
        <path
          opacity="0.9"
          d="M1107.59 1024L1107.59 -6.10351e-05L456.176 -6.10351e-05L1759 -6.10351e-05L1107.59 1024Z"
          fill="#181168"
        />
      </svg>
      <div className="text-white absolute inset-0 z-10 flex flex-col justify-center items-center text-center small:text-left small:justify-end small:items-start small:p-32">
        <h1 className="grand-title text-2xl-regular max-w-xl">
          Imagine Doing Math: Prime Integration
        </h1>
        <Image
          src="/logo.png"
          width="220px"
          height="230px"
          loading="eager"
          priority={true}
          quality={90}
          objectFit="cover"
          alt="Primes as a Service Logo"
          draggable="false"
          className="logo"
        />
        <h1
          id="more-nums"
          className="text-2xl-semi mb-4 drop-shadow-md shadow-black"
        >
          More numbers are finally here!
        </h1>
        <p className="text-base-regular max-w-[32rem] mb-6 drop-shadow-md shadow-black">
          Lol we sell primes
        </p>
        <UnderlineLink href="/store">Explore products</UnderlineLink>
      </div>
    </div>
  )
}

export default Hero
